"""tests for familiar-gemini"""

from __future__ import annotations

from unittest.mock import patch

import pytest
from familiar.agents import load_agents

from familiar_gemini import GeminiAgent


class TestGeminiAgent:
    """tests for gemini agent"""

    def test_registers_as_familiar_agent(self):
        assert isinstance(load_agents()["gemini"], GeminiAgent)

    def test_supports_skills(self):
        assert GeminiAgent().supports_skills() is True

    def test_name(self):
        agent = GeminiAgent()
        assert agent.name == "gemini"

    def test_output_file(self):
        agent = GeminiAgent()
        assert agent.output_file == "GEMINI.md"

    def test_skill_path(self, tmp_path):
        agent = GeminiAgent()
        path = agent.skill_path(tmp_path, "review")
        assert path == tmp_path / ".gemini" / "skills" / "review" / "SKILL.md"

    def test_supports_subagents(self):
        agent = GeminiAgent()
        assert agent.supports_subagents() is True

    def test_subagent_path(self, tmp_path):
        agent = GeminiAgent()
        path = agent.subagent_path(tmp_path, "python_sec")
        assert path == tmp_path / ".gemini" / "agents" / "python_sec.md"

    @pytest.mark.parametrize("name", ["_ops", "_"])
    def test_subagent_path_rejects_leading_underscore(self, tmp_path, name):
        agent = GeminiAgent()
        with pytest.raises(ValueError, match="starts with '_'"):
            agent.subagent_path(tmp_path, name)

    @pytest.mark.parametrize(
        ("headless", "auto", "approval_mode", "env", "argv"),
        [
            (True, False, None, None, ["gemini", "-p", "p"]),
            (False, False, None, None, ["gemini", "-i", "p"]),
            (False, True, None, None, ["gemini", "--approval-mode=yolo", "-i", "p"]),
            (True, True, None, None, ["gemini", "--approval-mode=yolo", "-p", "p"]),
            *(
                (
                    True,
                    True,
                    mode,
                    None,
                    ["gemini", f"--approval-mode={mode}", "-p", "p"],
                )
                for mode in ["default", "auto_edit", "yolo", "plan"]
            ),
            (
                True,
                True,
                None,
                "auto_edit",
                ["gemini", "--approval-mode=auto_edit", "-p", "p"],
            ),
            (
                True,
                True,
                "auto_edit",
                "plan",
                ["gemini", "--approval-mode=auto_edit", "-p", "p"],
            ),
            (True, False, "auto_edit", None, ["gemini", "-p", "p"]),
            (True, True, None, "", ["gemini", "--approval-mode=yolo", "-p", "p"]),
            (
                True,
                True,
                "default",
                "bogus",
                ["gemini", "--approval-mode=default", "-p", "p"],
            ),
        ],
        ids=[
            "headless",
            "interactive",
            "auto",
            "headless-auto",
            "param-default",
            "param-auto_edit",
            "param-yolo",
            "param-plan",
            "env",
            "param-over-env",
            "mode-ignored-without-auto",
            "empty-env-falls-to-default",
            "valid-param-over-invalid-env",
        ],
    )
    def test_run(self, tmp_path, monkeypatch, headless, auto, approval_mode, env, argv):
        if env is None:
            monkeypatch.delenv("FAMILIAR_GEMINI_APPROVAL_MODE", raising=False)
        else:
            monkeypatch.setenv("FAMILIAR_GEMINI_APPROVAL_MODE", env)

        with patch("familiar_gemini.subprocess.call", return_value=0) as mock_call:
            result = GeminiAgent().run(
                tmp_path, "p", headless=headless, auto=auto, approval_mode=approval_mode
            )
        assert result == 0
        mock_call.assert_called_once_with(argv, cwd=tmp_path)

    @pytest.mark.parametrize(("headless", "rc"), [(True, 42), (False, 1)])
    def test_run_returns_exit_code(self, tmp_path, headless, rc):
        with patch("familiar_gemini.subprocess.call", return_value=rc):
            assert GeminiAgent().run(tmp_path, "prompt", headless=headless) == rc

    @pytest.mark.parametrize(
        ("approval_mode", "env"),
        [
            *((mode, None) for mode in ["bogus", "prompt", "reject", "auto-edit"]),
            (None, "bogus"),
        ],
    )
    def test_run_auto_invalid_approval_mode(
        self, tmp_path, monkeypatch, approval_mode, env
    ):
        if env is None:
            monkeypatch.delenv("FAMILIAR_GEMINI_APPROVAL_MODE", raising=False)
        else:
            monkeypatch.setenv("FAMILIAR_GEMINI_APPROVAL_MODE", env)

        with (
            patch("familiar_gemini.subprocess.call") as mock_call,
            pytest.raises(ValueError, match="invalid approval mode"),
        ):
            GeminiAgent().run(
                tmp_path, "p", headless=True, auto=True, approval_mode=approval_mode
            )
        mock_call.assert_not_called()

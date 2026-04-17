"""gemini cli agent plugin for familiar"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from familiar.agents import Agent

VALID_APPROVAL_MODES = frozenset({"yolo", "prompt", "reject"})
DEFAULT_APPROVAL_MODE = "yolo"


class GeminiAgent(Agent):
    """agent that uses the gemini cli"""

    name = "gemini"
    output_file = "GEMINI.md"
    skill_dir = ".gemini/skills"
    subagent_dir = ".gemini/subagents"

    def run(
        self,
        repo_root: Path,
        prompt: str,
        headless: bool,
        auto: bool = False,
        approval_mode: str | None = None,
    ) -> int:
        cmd = ["gemini"]
        if auto:
            mode = (
                approval_mode
                or os.environ.get("FAMILIAR_GEMINI_APPROVAL_MODE")
                or DEFAULT_APPROVAL_MODE
            )
            if mode not in VALID_APPROVAL_MODES:
                raise ValueError(
                    f"invalid approval mode {mode!r},"
                    f" expected one of {sorted(VALID_APPROVAL_MODES)}"
                )
            cmd.append(f"--approval-mode={mode}")
        if headless:
            cmd.extend(["-p", prompt])
        else:
            cmd.extend(["-i", prompt])
        return subprocess.call(cmd, cwd=repo_root)

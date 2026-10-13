# changelog

## 0.3.1 - 2026-10-14

- fix `--save-subagent` to write `.gemini/agents/<name>.md`, where gemini cli loads project agents; `.gemini/subagents/<name>/AGENT.md` was never read. gemini also needs `name` and `description` frontmatter, which familiar-cli 0.6.1 and earlier don't write. subagent names starting with `_` now raise an error, since gemini skips those files
- fix approval modes to match gemini cli's `--approval-mode`: valid values are now `default`, `auto_edit`, `yolo` and `plan`. `prompt` and `reject` were never accepted by gemini (it exited at startup) and now raise an error instead

## 0.3.0 - 2026-04-26

- **configurable approval mode**: `approval_mode` parameter on `GeminiAgent.run()` and `FAMILIAR_GEMINI_APPROVAL_MODE` env var allow overriding the default `yolo` mode (valid: `yolo`, `prompt`, `reject`)
- fix `familiar-cli` version requirement in readme (was `>=0.3.1`, now `>=0.4.0`)

## 0.2.0 - 2026-02-16

- add gemini skill and subagent path definitions for familiar `--save-skill` and `--save-subagent` support
- require `familiar-cli>=0.4.0`
- add release SBOM generation and upload (CycloneDX)

## 0.1.1

- **auto mode**: added `auto` parameter to `GeminiAgent.run()`, passes `--approval-mode=yolo` flag to gemini cli when enabled.

## 0.1.0

initial release

- `GeminiAgent` plugin for [familiar](https://github.com/cyberwitchery/familiar)
- supports headless and interactive modes
- requires `gemini` cli in path

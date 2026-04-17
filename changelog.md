# changelog

## unreleased

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

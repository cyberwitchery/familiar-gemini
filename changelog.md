# changelog

## unreleased

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

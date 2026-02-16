# familiar-gemini

gemini cli agent plugin for [familiar](https://github.com/cyberwitchery/familiar)

## installation

```bash
pip install familiar-gemini
```

## usage

once installed, the `gemini` agent becomes available in familiar:

```bash
familiar conjure gemini python sec
familiar invoke gemini bootstrap-python myapp cli
```

save composed conjurings as reusable gemini subagents:

```bash
familiar conjure gemini python sec --save-subagent
familiar conjure gemini rust infra --save-subagent --subagent-name ship_ops
```

save invocations as reusable gemini skills:

```bash
familiar invoke gemini code-review --save-skill
familiar invoke gemini refactor src/foo.py --save-skill --skill-name cleanup_refactor
```

## requirements

- [familiar-cli](https://github.com/cyberwitchery/familiar) >= 0.3.1
- [gemini cli](https://github.com/google/gemini-cli) installed and in path

# 🎄 Advent of Code Monorepo 🎄

## 🎄 Summary 🎄

These are my solutions for the [Advent of Code](https://adventofcode.com) challenges.  Each year is imported as a git subtree for previous years (before 2025).  I have only attempted these problems in python as that is my main language I use.  

### Launch.json
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debug with Fixed Arg",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            // "args": ["day"]
        },
        {
            "name": "Python: Run with Runtime Arg",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            // "args": ["day"]
        }
    ]
}
```
### settings.json
```json
    "editor.formatOnSave": false,
    "editor.wordWrap": "off",
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "python.defaultInterpreterPath": "${workspaceFolder}/2025/.venv",
    "terminal.integrated.shellIntegration.enabled": false,
    "terminal.integrated.shellIntegration.decorationsEnabled": false,
```


Year specific README's will contain any additional information
# 🎄 Advent of Code Monorepo 🎄

## 🎄 Summary 🎄

These are my solutions for the [Advent of Code](https://adventofcode.com) challenges.  Each year is imported as a git subtree for previous years (before 2025).  I have only attempted these problems in python as that is my main language I use.  


## Basic Structure

Each year is self contained to represent different years tools and / or files.  Normally it will be structured as follows. 

```terminal 
    |────AdventOfCode
    |    ├── .vscode                    <- .vscode folder
    |    |   ├── launch.json            <- json launch file
    |    |   └── settings.json          <- json settings file
    |    ├── 2023                       <- Year attempt
    |    ├── 2024                       <- Year attempt
    |    ├── 2025                       <- Year attempt
    |    |   ├── .venv                  <- Virtual environment for that year
    |    |   ├── day1.py                <- Day1 py file
    |    |   ├── day2.py                <- Day2 py file
    |    |   ├── poetry.lock            <- Locked file of libarary dependency versions
    |    |   └── pyproject.toml         <- Toml file with main libraries
    |    ├── secret                     <- Year attempt
    |    |   └── cookie.text            <- Holds your cookie string
    |    ├── utils                      <- Utils Folder
    |    |   ├── __init__.py            <- For imports
    |    |   ├── day_template.py        <- Basic template for start
    |    |   ├── loc.py                 <- Py file to count lines of code
    |    |   ├── support.py             <- Houses other support functions for moving data
    |    |   └── time_run.py            <- Timing func
    |    ├── .gitignore                 <- .gitignore file for keeping files out of github
    |    └── README.md                  <- Overall README for monorepo
```

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
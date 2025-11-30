# 🎄 Advent of Code 🎄

## 🎄 Summary 🎄

These are my solutions for the [Advent of Code](https://adventofcode.com) challenges.  Each year is imported as a git subtree for previous years (before 2025).  I have only attempted these problems in python as that is my main language I use.  


## Basic Structure

Each year is self contained to represent different years tools and / or files.  Normally it will be structured as follows. 

```terminal 
    |────AdventOfCode
    |    ├── .vscode              <- .vscode folder
    |    |   ├── launch.json      <- json launch file
    |    |   └── settings.json    <- json settings file
    |    |
    |    ├── 2023                 <- Year attempt
    |    ├── 2024                 <- Year attempt
    |    ├── 2025                 <- Year attempt
    |    |   ├── .venv            <- Virtual environment for that year
    |    |   ├── day1.py          <- Day1 py file
    |    |   ├── day2.py          <- Day2 py file
    |    |   ├── poetry.lock      <- Lock file of libarary dependency versions
    |    |   └── pyproject.toml   <- Toml file with main libraries
    |    |
    |    ├── secret               <- For the secrets
    |    |   ├── cookie.text      <- C is for cookie!!!!
    |    |   └── last.text        <- Submits your email as a UA header.  So Eric can contact you if youre hammering his server
    |    |
    |    ├── utils                <- Utils Folder
    |    |   ├── __init__.py      <- For module imports
    |    |   ├── day_template.py  <- Basic template for start
    |    |   ├── loc.py           <- Py file to count lines of code
    |    |   └── support.py       <- Support functions for supporting actions
    |    |
    |    ├── .gitignore           <- .gitignore file for keeping files out of github
    |    ├── .cache.bak           <- cache
    |    ├── .cache.dat           <- moves
    |    ├── .cache.dir           <- everything around me (temp files that store the scraped data)
    |    └── README.md            <- Overall README for monorepo
```

### File running

Being that there are multiple years here, file running can get a little tricky.  One way around it is to point your settings.json to whatever year you're working on as included in the sample below.  That will activate the appropriate years venv for usage in VSCode.  You also can run files as modules `python -m 2020.day1` which means you could remove giant line at the beginning of each script that adds the root folder to the path temporarily.  Up to you!

### Launch.json
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Run with Runtime Arg",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            // ["day"]
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
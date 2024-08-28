# MyPeopleGame - API

The API of [the game to create people](https://github.com/Krosmez/MyPeopleGame)

## Install

```sh
python --version
# At least 3.10.6

python -m pip install -U virtualenv
python -m virtualenv venv

# Windows 
venv\Scripts\activate
# UNIX / MacOS
source ./venv/bin/activate

pip install -r requirements.txt
```

## Launch

```sh
# Windows 
venv\Scripts\activate
# UNIX / MacOS
source ./venv/bin/activate

fastapi dev main.py
```

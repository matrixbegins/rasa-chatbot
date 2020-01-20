## Restaurant Finder chatbot RASA

A simple chatbot built on rasa for restaurant recommendation based on given preferences.

## Installation
You'll need python 3.6+, rasa 1.6.1, rasa-sdk 1.6.1, rasa-x 0.24.1(optional)
for more requirements details please refer [requirements.txt](requirements.txt)

### Steps:

```
# get the code
git clone git@github.com:matrixbegins/rasa-chatbot.git
cd rasa-chatbot.git

# make virtual env
python3 -m venv ./venv

# activate venv
source venv/bin/activate

# install dependecies
pip3 install -r requirements.txt

```

## Running the bot
```
# Training the bot
> rasa train nlu
> rasa train core

# in one terminal launch action server by running
> rasa run actions

in different tab launch rasa server
> rasa run
# or
> rasa shell

# for troubleshooting and debugging use following:
> rasa run --debug
# or
> rasa shell --debug

```

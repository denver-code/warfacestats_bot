# WarfaceStatsBot - International
[![made-with-python3](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/denver-code/warfacestats_bot/issues/new)
[![LICENSE !](https://github.com/denver-code/warfacestats_bot/blob/master/LICENSE)](https://github.com/denver-code/warfacestats_bot/blob/master/LICENSE) 
[![PRODUCTION !](https://img.shields.io/badge/Production-1f425f.svg)](https://t.me/warfacestats_bot  ) 
<p align="center">
    <a href="https://wf.my.com"><img height="128" src="https://i.imgur.com/AB5fREI.png"></a> <a href="https://discord.com"><img src="https://telegram.org/img/t_logo.png?1"></a> <br>
    Warface Telegram bot with useful tools for the community.
</p>

> [!NOTE]   
> Realtime work version located: https://t.me/warfacestats_bot  
   
Among the tools you could find there is stuff like checking
current amount of online player per channel, game news,
reference to useful materials, game ladders, player statistics
and more to come. The list of available commands will be registered in the /help command!

## Env Information
Most configuration really isn't about the app -- it's about where the app runs, what keys it needs to communicate with third party API's, the db password and username, etc... They're just deployment details -- and there are lots of tools to help manage environment variables -- not the least handy being a simple .env file with all your settings. Simply source the appropriate env before you launch the app in the given env (you could make it part of a launch script, for instance).

env files look like this:

    SOMEVAR="somevalue"
    ANOTHERVAR="anothervalue"

To source it:
``` Bash
    $ source sample.env  # or staging.env, or production.env, depending on where you're deploying to
```
## Run gateway server
> [!NOTE]
> We used python 3.10.1 64-bit version!  
> And don't forget to change your .env settings!  
``` Bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

## Run gateway in docker with scripts
> [!NOTE]  
> Install docker  
``` Bash
$ sudo sh scripts/runbot.sh
```

## Run gateway in docker with docker-compose
``` Bash
$ sudo docker-compose up --build -d
```

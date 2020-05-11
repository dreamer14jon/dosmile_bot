# dosmile_bot
Dosmile Telegram bot: unleash the power of Dandelion Sentiment API!
[![Run on Repl.it](https://repl.it/badge/github/lonlylocly/dosmile_bot)](https://repl.it/github/lonlylocly/dosmile_bot)
![Sample conversation with the bot](https://raw.githubusercontent.com/lonlylocly/dosmile_bot/master/sample_conversation.jpg)

## What is this?

In this repo you may find a simple [Telegram](https://telegram.org/) bot that uses [Dandelion Sentiment Analysys API](https://dandelion.eu/docs/api/datatxt/sent/v1/) and is written in Python. 
It replys with an emoji to each message you send, based on how positive or negative was the text of the message.

One may consider this as an example of simple Telegram bot, or as a starting point with Dandelion API.

## How do I make a Telegram bot?

You should start with creating a bot. Just follow the instructions [here](https://core.telegram.org/bots).
For this bot [telepot](https://github.com/nickoala/telepot) Python library is used.

## How do I use Dandelion API?

First of all, sign up for the Dandelion API free trial [here](https://dandelion.eu/accounts/register/?next=/semantic-text/entity-extraction-demo/), if you didn't do that yet! The trial does not expire, it gives you generous amount of credit per day, which is more than enough to "get your feet wet", as Italians say :)

There is a pretty nice demo of the [Sentiment Analysis API](https://dandelion.eu/semantic-text/sentiment-analysis-demo/?appid=it%3A333903271&exec=true), which is just one of the features of Dandelion. Don't miss the demo of the [Named Entity Recognition API](https://dandelion.eu/semantic-text/entity-extraction-demo/?text=The+Mona+Lisa+is+a+16th+century+oil+painting+created+by+Leonardo.+It%27s+held+at+the+Louvre+in+Paris.&lang=auto&min_confidence=0.6&exec=true#results)!

## Installing & running 

```
$ mkvirtualenv --python=/usr/bin/python3.4 -r requirements.txt bot
$ python -u dosmile.py
```



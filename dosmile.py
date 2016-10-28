# -*- coding: utf-8 -*-
import requests
import pprint
import asyncio
import logging
import json

import telepot
import telepot.async

settings = json.load(open("settings.json", "r"))

app_id=settings["app_id"]
app_key=settings["app_key"]
token = settings["token"]

endpoint="https://api.dandelion.eu/datatxt/sent/v1?text={text}&$app_id={app_id}&$app_key={app_key}"

positive = ["😌", "😊", "😄"]
negative = ["😒", "😠", "😡"]
neutral = "😐"

class DoSmileBot(telepot.async.Bot):
    def __init__(self, *args, **kwargs):
        self.queries_cache = {}
        super(DoSmileBot, self).__init__(*args, **kwargs)

        self._answerer = telepot.async.helper.Answerer(self)

    def get_clean_reply(self, message_text):
        resp = self.lookup_query(message_text)
        pprint.pprint(resp)
        if "error" in resp:
            raise Exception("Failed to get reply: %s" % resp) 

        sent = resp.get("sentiment", {})
        repl_emoji = self.get_emoji_reply(sent)

        return repl_emoji

    # Since the reply to the same query will be always the same, we cache it
    def lookup_query(self, message_text):
        query = message_text.strip().lower()
        if query not in self.queries_cache:
            q = endpoint.format(text=message_text, app_id=app_id, app_key=app_key)
            print(q)
            resp = requests.get(q)
            if len(self.queries_cache) > 100000:
                self.queries_cache.pop(list(self.queries_cache)[0])
            self.queries_cache[query] = resp.json()
        else:
            print("Found in cache")

        return self.queries_cache[query]

    def get_emoji_reply(self, sent):
        pprint.pprint(sent)
        try:
            score = float(sent["score"])
            sent_type = sent["type"]
            if sent_type == "neutral":
                return neutral
            elif sent_type == "positive":
                if score >= 0 and score <=0.4:
                    return positive[0]
                elif score >0.4 and score <=0.75:
                    return positive[1]
                else:
                    return positive[2]
            elif sent_type == "negative":
                if score >= -1.0 and score <= -0.8:
                    return negative[2]
                elif score > -0.8 and score <= - 0.4:
                    return negative[1]
                else:
                    return negative[0]
        except Exception as e:
            logging.exception("Failed to lookup emoji")
            return None

    def get_custom_reply(self, chat_id, message_text):
        try:
            repl_emoji = self.get_clean_reply(message_text)
            if repl_emoji is not None:
                return repl_emoji
            else:
                return "Sorry, I am so broken..."
        except Exception as e:
            logging.exception("Failed to get reply")
            return "Sorry, I am probably broken..."

    @asyncio.coroutine
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        message_text = msg.get('text', '')
        user_id = msg["from"]["id"]
        if message_text == '/start':
            yield from self.sendMessage(chat_id, "Ciao!")
            yield from self.sendMessage(chat_id, "I am dosmile_bot. Do you think you can make me smile or frown? Talk to me in English or Italian.")
            return
        try:
            yield from self.sendMessage(chat_id, self.get_custom_reply(chat_id, message_text))
        except Exception as e:
            print(e)


bot = DoSmileBot(token)
loop = asyncio.get_event_loop()

loop.create_task(bot.message_loop())
print('Listening ...')

loop.run_forever()

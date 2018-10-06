#!/usr/bin/env python

import json
import tornado.ioloop
import tornado.web
from gtts import gTTS
import pyttsx
import random
import uuid


def generate_random_voice():
    gender = random.choice(['male', 'female'])
    age = random.randint(20, 65)
    return pyttsx.voice.Voice(id=uuid.uuid4(), gender=gender, age=age)


class TextHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        text = data.get("text", "Just a Test.")

        # gTTS
        tts = gTTS(text=text, lang='en')
        tts.save("post_tts.mp3")

        #pyttsx
        engine = pyttsx.init()
        for sentence in text.split("."):
            voice = generate_random_voice()
            print voice
            engine.setProperty('voice', voice.id)
            engine.setProperty('rate', random.randint(10,20))
            engine.say(sentence)
        engine.runAndWait()


def make_app():
    return tornado.web.Application([
        (r"/", TextHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

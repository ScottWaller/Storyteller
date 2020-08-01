#!/usr/bin/env python

import argparse
import pyttsx3
import random
import uuid
import subprocess

MALE = "male"
FEMALE = "female"

FILENAME = "TEST"

class Speaker(object):
    """docstring for Speaker"""
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.voice = generate_voice(name, gender)

    def speak(self, text, engine):
        engine.setProperty('voice', self.voice.id)
        engine.setProperty('rate', random.randint(50,100))
        engine.say(text)
        engine.save_to_file(text, FILENAME)
        engine.runAndWait()


def find_speaker(text):
    return random.choice([Speaker("mary", FEMALE)])


def generate_voice(name, gender, age=30):
    return pyttsx3.voice.Voice(id=name, name=name, gender=gender, age=age)


def parse_args():
    parser = argparse.ArgumentParser("Command Line utility for generating tts with different voices")
    parser.add_argument("--text")
    return parser.parse_args()

def main():
    args = parse_args()
    text = args.text
    sentences = text.split(".")

    #pyttsx3
    engine = pyttsx3.init()
    # for sentence in text.split("."):
    #     voice = generate_random_voice()
    #     print voice
    #     engine.setProperty('voice', voice.id)
    #     engine.setProperty('rate', random.randint(50,100))
    #     engine.say(sentence)
    # engine.runAndWait()
    speakers = set([])
    for sentence in sentences:
        speaker = find_speaker(sentence)
        if speaker not in speakers:
            speakers.add(speaker)

        speaker.speak(sentence, engine)


if __name__ == "__main__":
    main()

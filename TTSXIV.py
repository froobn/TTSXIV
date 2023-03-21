import asyncio
import json
import random

import api

import websockets
from NBSapi import NBSapi
from urllib.request import urlretrieve
from audioplayer import AudioPlayer
import audioread
import os
import re

configFile = open("config.json")
config = json.load(configFile)
configFile.close()
assert(config['apikey'] != "")

port = str(config['port']) #PORT NUMBER FOR WEBSOCKET
rate = config['sapirate'] #SAPI5 TTS SPEECH RATE, -10 to 10

tts = NBSapi()
tts.SetRate(rate)

api.import_voices()
speakerdata = open("voices.json")
coquiSpeakers = json.load(speakerdata)

male = []
female = []

for index, voice in enumerate(tts.GetVoices()):
    print(voice)
    if "Microsoft" in voice['Name'] and "Mary" not in voice['Name'] and "Mike" not in voice['Name']:
        if "Female" in voice['Gender']:
            female.append(index)
        else:
            male.append(index)
                 
defaultvoice = male[0]

audio_time = 0

AP = None
file_swap = 0


def duration_detector(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
  
    return hours, mins, seconds


async def main():
    async with websockets.connect("ws://localhost:"+port+"/Messages") as websocket:
        try:
            while True:
                rsp = await websocket.recv()
                data = json.loads(rsp)
                if data['Type'] == 'Say':
                    say(data)
                if data['Type'] == 'Cancel':
                    cancel()   
        except KeyboardInterrupt:
            pass
        
def say(data):
    speaker = data['Speaker']
    payload = data['Payload']
    voice = data['Voice']
    global AP
    if AP:
        AP.stop()
    coquiSpeaker = speaker.lower()
    coquiSpeaker = re.sub(r"[^a-z]+", '', coquiSpeaker)
    if coquiSpeakers.get(coquiSpeaker): 
        try:
            global playback
            global file_swap
            url = api.get_sample(coquiSpeakers[coquiSpeaker], coquiSpeaker, payload, speed=0.7)
            if url:
                global audio_time   
                if file_swap:
                    file_swap = 0
                else:
                    file_swap = 1
                urlretrieve(url, "temp/temp"+str(file_swap)+".wav")
                
                AP = AudioPlayer("temp/temp"+str(file_swap)+".wav")
                AP.play()
                with audioread.audio_open("temp/temp"+str(file_swap)+".wav") as f:
                    audio_time += f.duration
                    hours, mins, seconds = duration_detector(int(audio_time))
                    os.system('cls')
                    print('Session Synthesis Time: {}:{}:{}'.format(hours, mins, seconds))
                return
        except:
            pass    
    if 'Name' in voice:
        if voice['Name'] == 'Male':
            random.seed(speaker)
            voiceIndex = random.choice(male)
            tts.SetVoice(voiceIndex)
        elif voice['Name'] == 'Female':
            random.seed(speaker)
            voiceIndex = random.choice(female)
            tts.SetVoice(voiceIndex)
        else:
            tts.SetVoice(defaultvoice)
    tts.Speak(payload, 1) # SAPI
    
def cancel():
    global AP
    tts.Stop() # SAPI
    if AP:
        AP.stop()

def play_audio(file_path):
    global playback
    playback = AudioPlayer(file_path)
    playback.play()


def is_coquispeaker(speaker):
    for voice in coquiSpeakers.keys():
        if voice == speaker:
            return True
    return False
    
asyncio.run(main())
if AP:
    AP.close()
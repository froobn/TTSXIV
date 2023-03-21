import json
import requests

configFile = open("config.json")
config = json.load(configFile)
configFile.close()
key = config['apikey']
sampleroot = 'https://app.coqui.ai/api/v2/samples'


def get_sample(voice_id, voice_name, text, speed=0.75, emotion="Neutral",authkey=key):
    headers= {
        "Authorization": "Bearer "+ authkey,
    }
    data = {
        "voice_id": voice_id,
        "emotion": emotion,
        "name": voice_name,
        "text": text,
        "speed": speed
    }
    try:
        f = open("temp/temp.json", 'w')
        response = requests.post(sampleroot, headers=headers, data=data)
        data = json.loads(response.text)
        url = data.get('audio_url')
        f.write(response.text)
        f.close()
        return url
    except:
        return None
    
def import_voices(authkey=key):
    voiceroot = 'https://app.coqui.ai/api/v2/voices'

    headers= {
        "Authorization": "Bearer "+ authkey,
    }
    response = requests.get(voiceroot, headers=headers)
    data = json.loads(response.text)
    voice_dict = {}
    for voice in data['result']:
        voice_dict[voice['name']] = voice['id']
    with open('voices.json', 'w') as convert_file:
        convert_file.write(json.dumps(voice_dict, indent=4))

import json
import requests
import os

directory = 'data'
configFile = open("config.json")
config = json.load(configFile)
configFile.close()

authkey = config['apikey']
voiceroot = "https://app.coqui.ai/api/v2/voices"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    f = f.replace(os.sep, '/')
    # checking if it is a file
    name = os.path.splitext(filename)[0]
    print(name, f)
    headers = {
        "content_type": 'multipart/form-data; boundary=---011000010111000001101001',
        "Authorization": "Bearer " + authkey
    }
    files = {'file': open(f, 'rb')}
    data = {
        "name": name,
        "file": f
    }
    response = requests.post(voiceroot, headers=headers, data=data, files=files)
    print(response)


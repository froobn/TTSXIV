TTSXIV SETUP INSTRUCTIONS - CoquiTTS:
*to run python files directly, install python of course, to run in terminal type
python filename.py to run*

1. create an account for gttps://app.coqui.ai
	as a free trial, you get 30 minutes of synthesis time free!
	after this you will have to pay 20$ per 4 fours of synthesis time for the custom voice usage
	
2. setup custom voices using populatevoices.py

3. grab an api key from https://app.coqui.ai/account (scroll to the bottom)
	COPY THIS KEY, YOU WILL ONLY SEE IT ONCE
	you can create new keys and disable old ones from this page aswell

4. configure config.json in TTSXIV directory with your apikey in encased in quotes
	ex: "apikey": "thisisasampleapikey",

5. in dalamud, install texttotalk from the main addon download screen,
	set the voice selection to be 'websocket',
	take note of the port used, or set the port to whatever you'd like

6. in config.json, configure the port number to the port number used by texttotalk
	you can also configure the SAPI TTS speech rate here (-10 to 10)

7. run TTSXIV.exe!

Huzzah!
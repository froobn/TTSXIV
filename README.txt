TTSXIV SETUP INSTRUCTIONS - CoquiTTS:
*to run python files directly, install python of course, to run in terminal type
python filename.py to run*
	I developed using python 3.7.1 

0. run 'pip install -r requirements.txt' in cmd to grab necessary libraries

1. create an account for https://app.coqui.ai
	as a free trial, you get 30 minutes of synthesis time free!
	after this you will have to pay 20$ per 4 fours of synthesis time for the custom voice usage
	
2. grab an api key from https://app.coqui.ai/account (scroll to the bottom)
	COPY THIS KEY, YOU WILL ONLY SEE IT ONCE
	you can create new keys and disable old ones from this page aswell

3. configure config.json in TTSXIV directory with your apikey in encased in quotes
	ex: "apikey": "thisisasampleapikey",

4. OPTIONAL: setup custom voices using populatevoices.py (or using POPULATEVOICES.bat) ALT: manually upload custom voice files at https://app.coqui.ai/studio
	you could also manually add any custom voices, BUT the program assumes that the voice name is lowercase and only alphabet characters!
	** if you run more than once, it could create duplicate voices, I'll probably create a quick solution soon, but for now make sure you visit https://app.coqui.ai/studio to manage your custom voices if needed

5. in dalamud, install texttotalk from the main addon download screen,
	set the voice selection to be 'websocket',
	take note of the port used, or set the port to whatever you'd like

6. in config.json, configure the port number to the port number used by texttotalk
	you can also configure the SAPI TTS speech rate here (-10 to 10)

7. run TTSXIV.py (or by using start.bat)

	- To install more SAPI5 voices, go to Speech Settings in Windows Settings, and install more voices (Ive only tested english based ones)

Huzzah!

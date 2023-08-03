
# Voice Cloning Demo  
## Directory structure
```
[srpraman/text_to_speech/](https://github.com/srpraman/text_to_speech/)
├── streamlit_app.py
├── requirements.txt
├── README.md
└── LICENSE
 
```
## Internal Logic
![Screenshot from 2023-08-03 20-29-49](https://github.com/srpraman/text_to_speech/assets/101314229/c73d1e6c-fab0-4043-8a11-dc0f3fe8459b)
**->  As the workflow diagram suggests, there are three key components which are working together.** 
   1. When you upload an audio file, it will use the AssemblyAI speech to text API key and immediately converts that audio file into to a transcript text file.
   2. Using OpenAI API key, the above transcript will get translated to Hindi (by default).
   3. At the end this translated text will be converted back to an audio file using ElevenLabs API key.     

## API keys
```
You are goinng to need three API keys to run this web app.
1. AssemblyAI API key
2. OpenAI API key
3. ElevenLabs API key
```

*For simplicity I have provided all the API keys except OpenAI key, because of security issue, so feel free to ask for the API key from me or you can generate yours.* 


## Instructions
1. This app is hosted on https://texttospeech-derwenjw4j.streamlit.app/ , so you can play with it or you can host this on your local machine, by cloning this repository and installing the requirements.txt file.
2. This app is still in its developmental stage so try to upload a small chunk of audio file (less than 60 seconds).


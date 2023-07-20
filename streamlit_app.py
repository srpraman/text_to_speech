# import packages
import streamlit as st
import assemblyai as aai
import openai
from elevenlabs import generate, play, set_api_key, save
from PIL import Image

# input parameters
input_file = 'yv60s-o2552.wav'
output_file = 'test.wav'
# aai.settings.api_key = "b976ef9d17e34196ab337daa2d0ae9eb"
# set_api_key("e47386203d3800a7d57840c1649afb38")

input_file = st.file_uploader("Choose a file")
if input_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
# host on web
	audio_file = open(input_file, 'rb')
	audio_bytes = audio_file.read()
	st.write("Input audio file")
	st.audio(audio_bytes)

'''# speech to text
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(input_file)
st.write(f'output of wav file: {transcript.text}')

# text translation
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
message = "convert this speech to Hindi:" + transcript.text 
if message:
	messages.append(
	{"role": "user", "content": message},
	)
	chat = openai.ChatCompletion.create(
		model="gpt-3.5-turbo", messages=messages
	)
reply = chat.choices[0].message.content
st.write(f"ChatGPT(Hindi): {reply}")

# text to speech
audio = generate(
    text=reply,
    voice="Arnold", model='eleven_multilingual_v1')
save(audio,output_file)

# web demo
st.write("Output audio file")
audio_file = open(output_file, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes)'''

# pipeline diagram
image = Image.open('worlflow.png')
st.image(image, caption='FLow Diagram')

# import packages
import streamlit as st
import assemblyai as aai
import openai
from elevenlabs import generate, play, set_api_key, save
from PIL import Image
from tempfile import NamedTemporaryFile

def stt(input_audio):
	aai.settings.api_key = "b976ef9d17e34196ab337daa2d0ae9eb"
	transcriber = aai.Transcriber()
	transcript = transcriber.transcribe(input_audio)
	return transcript.text

# text to text translation
def ttt(input_text, key, command = 'convert this speech to Hindi:'):
	openai.api_key = key
	messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
	message = command + input_text 
	if message:
		messages.append(
		{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	return reply

def tts(output_text):
	set_api_key("7ac11a92ad2fb0994f331ff7769911cd")
	audio = generate(
    text=output_text,
    voice="Arnold", model='eleven_multilingual_v1')
	# save(audio,output_file_name)
	# return output_file_name
	return audio

def main():

	input_file = st.file_uploader("Choose a file")
	if input_file is not None:
		with NamedTemporaryFile(suffix="wav") as temp:
			temp.write(input_file.getvalue())
			temp.seek(0)
        	# result = model.transcribe(temp.name)
		
		audio_bytes = input_file.read()
		st.write("Input audio file")
		st.audio(audio_bytes, format='audio/wav')
		save(audio_bytes, 'temp1.wav')
		itext = stt("temp1.wav")
		st.write(f'Transcript of your input file: {itext}')

		key = st.text_input('chatgpt api key', 'type here...')
		otext = ttt(itext, key)
		st.write(f"Hindi Translation: {otext}")

		output_file = tts(otext).read()
		st.write("Output audio file")
		st.audio(output_file, format='audio/wav')

	else:
		# pipeline diagram
		st.write("Nothing has been uploaded!!!!")

	image = Image.open('worlflow.png')
	st.image(image, caption='FLow Diagram')

main()




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



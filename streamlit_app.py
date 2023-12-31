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
def ttt(input_text, key, command = 'hindi'):
	openai.api_key = key
	messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
	message = 'convert this speech to ' + command + ":" + input_text 
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
	save(audio, 'temp1.wav')
	return audio
	

def main():

	input_file = st.file_uploader("Choose a file")
	if input_file is not None:
		audio_bytes = input_file.read()
		st.write("Input audio file")
		st.audio(audio_bytes, format='audio/wav')
		save(audio_bytes, 'temp1.wav')
		itext = stt("temp1.wav")
		st.write(f'Transcript of your input file: {itext}')

		key = st.text_input('chatgpt api key', 'type here...')
		lang = st.text_input('Language you wanted to translate to', 'e.g. hindi/spanish')
		otext = ttt(itext, key, command = lang)
		st.write(f"{lang} Translation: {otext}")

		output_file = tts(otext)
		st.write("Output audio file")
		st.audio(output_file, format='audio/wav')

	else:
		# pipeline diagram
		st.write("Nothing has been uploaded!!!!")

	image = Image.open('workflow.png')
	st.image(image, caption='Flow Diagram')

main()



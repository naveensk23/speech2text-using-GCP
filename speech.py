import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient.from_service_account_json("speech.json")

# Loads the audio into memory
with io.open('Abhi.flac', 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=48000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

print(response)

#for result in response.results:
#	print('Transcript: {}'.format(result.alternatives[0].transcript)
          
#print('Successfully Done')

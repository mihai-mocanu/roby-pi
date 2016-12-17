from chatterbot import ChatBot
from chatterbot.utils import input_function
import speech_recognition as sr
import pyttsx
import logging

# Uncomment the following line to enable verbose logging
logging.basicConfig(level=logging.INFO)

textToSpeech = pyttsx.init()
robyBot = ChatBot('Roby Hobby',
    storage_adapter = 'chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters = [
        'chatterbot.logic.BestMatch'
    ],
    filters = [
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter = 'chatterbot.input.TerminalAdapter',
    output_adapter = 'chatterbot.output.TerminalAdapter',
    database = 'roby-hobby-database',
    trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
robyBot.train("chatterbot.corpus.english")

print('Type something to begin...')

while True:
    try:
#        input_statement = robyBot.input.process_input_statement()
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)
	# recognize speech using Sphinx CMU
	try:
	    inputSR = r.recognize_sphinx(audio)
            statement, response, confidence = robyBot.generate_response(inputSR)
	    textToSpeech.say(response)
	    textToSpeech.runAndWait()
	except sr.UnknownValueError:
	    response = "Sphinx could not understand audio"
	except sr.RequestError as e:
	    response = "Sphinx error; {0}".format(e)
	textToSpeech.say(response)
	textToSpeech.runAndWait()

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break



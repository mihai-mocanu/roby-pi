from chatterbot import ChatBot
from chatterbot.utils import input_function
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
        input_statement = robyBot.input.process_input_statement()
        statement, response, confidence = robyBot.generate_response(input_statement)
	textToSpeech.say(response)
	textToSpeech.runAndWait()

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break



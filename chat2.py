from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot("Alex")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)

while True:
    userInput=input("User:")
    if userInput.strip()=="Bye" or userInput.strip()=="bye":
        print("Alex:Bye!")
        break;
    else:
        response=trainer.get_response(userInput)
        print(response)


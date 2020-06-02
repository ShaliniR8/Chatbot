from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot("Alex",storage_adapter="chatterbot.storage.MongoDatabaseAdapter")


trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")


def converse():
    while True:
        userInput=input("User:")
        if userInput.strip()=="Bye" or userInput.strip()=="bye":
            print("Alex:Bye!")
            break;
        else:
            response=chatbot.get_response(userInput) 
            print(response)


if __name__=="__main__":
    i=input("Enter START to start chatting\n")
    if i.strip()=="START":
        converse()
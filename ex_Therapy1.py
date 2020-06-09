#example of chatterbot using List Trainer

from chatbot import chatbot
from chatterbot.trainers import ListTrainer
import os



#entries=os.listdir('converse')
trainer=ListTrainer(chatbot)
trainer.train([
    "Hi there!",
    "Hello",
    "How are you",
    "I'm doing well, how are you?",
    "I'm bored",
    "Music might be a remedy to that!",
    "I'm really bored",
    "We can talk then",
    "What should we talk about?",
    "What do you wanna talk about?",
    "I want to know about Thyrocare?",
    "Thyrocare Technologies Limited is a chain of diagnostic and preventive care laboratories, based in Navi Mumbai."
    ])
trainer.train([
    "I am feeling down",
    "Why?",
    "I feel lonely",
    "You can talk to me anytime you feel lonely",
    "Thank you.",
    "You're welcome, I'm here to be your friend"
    ])
#for entry in entries:
#    chat=open('converse/'+entry,'r').readlines()
#    trainer.train(chat)
              
while True:
    userInput=input("Me:")
    if userInput.strip()=="Bye" or userInput=="bye":
        print("Bot:Bye!")
        break
    else:
        print(chatbot.get_response(userInput))
        

from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatbot import chatbot


conv= open("test.txt","r").readlines()
trainer=ListTrainer(chatbot)
trainer.train(conv)
trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

app = Flask(__name__)

'''
conv1=open("train1.txt","r").readlines()
trainer2=ListTrainer(english_bot)
trainer2.train(conv1)
'''

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()

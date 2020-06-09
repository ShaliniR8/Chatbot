#1. Login
#2. Be directed to website
#3. Be directed to Chat application
#4. Get response

from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chat2 import chatbot



#TRAINING IS DONE ONLY ONCE AFTER MAKING ANY CHANGE


#chatterbotcorpus training

chatbot.storage.drop()
trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")


#list training
'''
conv1=open("train1.txt","r").readlines()
trainer2=ListTrainer(english_bot)
trainer2.train(conv1)
'''

app = Flask(__name__)


#login
@app.route("/")
def home():
    try:
        return render_template("home.html")
    except:
        return "error"
#website
@app.route("/index")
def index():
    return render_template("index.html")

#chat
@app.route("/chat")
def chat():
    return render_template("chat.html")

#get response
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText.strip()=='Bye' or userText.strip()=='bye':
        return str("Bye!")
    else:
        return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)

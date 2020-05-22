from chatterbot.response_selection import get_most_frequent_response,get_first_response,get_random_response
from chatterbot.comparisons import levenshtein_distance,synset_distance,sentiment_comparison,jaccard_similarity
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

import pandas as pd


df=pd.read_csv("Response.csv",)
score=pd.read_csv("Score_Report.csv")
compare=[levenshtein_distance,synset_distance,sentiment_comparison,jaccard_similarity]
select=[get_most_frequent_response,get_first_response,get_random_response]


for i in range(len(compare)):
    for j in range(len(select)):
        chatbot = ChatBot(
            "Bot",
            statement_comparison_function=compare[i],
            logic_adapters=[
                    {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'response_selection_method':select[j] ,
                    }],
            
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
        )
                
        trainer=ChatterBotCorpusTrainer(chatbot)
        trainer.train("chatterbot.corpus.english")
        test_conv=open("test.txt","r")
        col="Bot{num}".format(num=i+j+1)
        resp=[]
        sc=[]
        for t in test_conv.readlines():
            print(t)
            r=chatbot.get_response(t.strip())
            resp.append(r)
            sc.append(chatbot.get_response(t.strip()).confidence)
            print("This frame completed")

        print(resp,sc)
        df.insert(1,col,resp)
        score.insert(0,col,sc)
        print(df[col],score[col])
            
df.to_csv (r'C:\Users\KIIT\Project\Response.csv', index = False, header=True)
score.to_csv(r'C:\Users\KIIT\Project\Score_Report.csv', index = False, header=True)




from chatterbot import response_selection
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.comparisons import sentiment_comparison
import logging


chatbot = ChatBot(
    "Friend",
    logic_adapters=[
            {
            'import_path': 'chatterbot.logic.BestMatch',
            'response_selection_method': response_selection.get_most_frequent_response,
            'maximum_similarity_threshold': 0.85
            }
    ],
    statement_comparison_function=sentiment_comparison,
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
)


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from nltk.corpus import wordnet as wn
from train import name_identifier
import random

mybot = ChatBot(name='Zara', read_only=False, logic_adapters=
               ['chatterbot.logic.MathematicalEvaluation',
               'chatterbot.logic.BestMatch'])

#data = prepared_data('training.txt')

list_trainer = ListTrainer(mybot)

#After the model is trained one time, and no any changes applied, comment the below lines
#corpus_trainer = ChatterBotCorpusTrainer(mybot)
#corpus_trainer.train('chatterbot.corpus.english')


me = ['I am Zara', 'My name is Zara', 'Zara']
w_question = "what is a"

def reply_ans_for_name():
    return random.choice(me)

def clean_string(data):
    data = data + " "
    x = len(data) - 1
    temp = ''
    
    while x > 0:
        if data[x] == '\\': break
        temp = temp + data[x]
        x = x - 1
    return temp [::-1]
    
def clean(data_list):
    temp_list = []

def get_response(msg):
    
    if name_identifier(msg):
        res = str(reply_ans_for_name())
        return res
    
    elif msg.lower().startswith(w_question) and (msg.lower().find('my') == -1 and msg.lower().find('your') == -1):
            msg=msg.split(); msg=msg[-1:]
            msg="".join(msg); msg=msg+'.n.01'
            definition_finder = wn.synset(msg).definition()
            
            return definition_finder
            
    else:
        res = str(mybot.get_response(msg))
        return res


if __name__ == "__main__":
    pass
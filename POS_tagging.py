__author__ = 'Chandima'

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenism = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenism:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

# process_content()


def process_sentence(sentence):

    token_list = custom_sent_tokenizer.tokenize(sentence)

    try:
        for i in token_list:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))


process_sentence("I ate the spaghetti with meatballs.")

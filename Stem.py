__author__ = 'Chandima'

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["kill", "killed", "killing", "killer", "kills"]

for w in example_words:
    print(ps.stem(w))

new_text = "It is very import to be kill the killer in the killing area to kills to be stopped."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

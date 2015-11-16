__author__ = 'Chandima'

from nltk import sent_tokenize
from nltk import word_tokenize

example_text = "I love Hansi. Do you love me too?"
print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)

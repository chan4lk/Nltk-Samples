__author__ = 'Chandima'

import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
print(nltk.__file__)

sample = gutenberg.raw("bible-kjv.txt")

tokens = sent_tokenize(sample)
for sent in tokens[:15]:
    print(sent)
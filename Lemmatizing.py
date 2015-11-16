__author__ = 'Chandima'

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize(word="better", pos='a'))
print(lemmatizer.lemmatize(word="cats"))
print(lemmatizer.lemmatize(word="run"))
print(lemmatizer.lemmatize(word="run", pos='v'))
print(lemmatizer.lemmatize(word='geese'))
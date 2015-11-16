__author__ = 'Chandima'

import nltk
import pickle
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(15))
# print(all_words["stupid"])

word_features = list(all_words.keys())[:3000]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

feature_sets = [(find_features(rev), category) for (rev, category) in documents]

training_set = feature_sets[:1900]
testing_set = feature_sets[1900:]

# posterior = prior occurrences x likelihood / evidence

# #classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naviebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes algo accuracy:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

# #save_classifier = open("naviebayes.pickle", "wb")
# #pickle.dump(classifier, save_classifier)
# #save_classifier.close()

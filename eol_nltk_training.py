#!/usr/bin/env python
# coding: utf-8

import nltk
from nltk.corpus.reader import CategorizedPlaintextCorpusReader

corpus_root = '/Users/athessen/nltk_data/corpora/eco'
reader = CategorizedPlaintextCorpusReader(corpus_root,r'lion|shark\d*\.txt',cat_file='cats.txt')
print reader.fileids()

print reader.categories()


"""
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000] [1]

def document_features(document): [2]
    document_words = set(document) [3]
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
"""
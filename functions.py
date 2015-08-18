"""Contains some functions"""

import pickle
import data
from random import randrange


def save_scores(filename, object):
    with open(filename, 'wb') as file:
        pick = pickle.Pickler(file)
        pick.dump(object)


def get_scores(filename):
    with open(filename, 'rb') as file:
        unpick = pickle.Unpickler(file)
        scores = unpick.load()

    return scores


def get_random_word(words):
    rdm_index = randrange(len(data.words))

    return data.words[rdm_index]


def get_hidden_word(word):
    rdm_word_hidden = str()
    i = 0

    while i < len(word):
        rdm_word_hidden += "*"
        i += 1

    return rdm_word_hidden

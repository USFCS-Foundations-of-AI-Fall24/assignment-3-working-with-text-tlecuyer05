## A representation of a document as a set of tokens.

from collections import defaultdict
from math import sqrt

class Document :
    def __init__(self, true_class=None):
        self.true_class = true_class
        self.tokens = defaultdict(lambda:0)

    def add_tokens(self, token_list) :
        for item in token_list :
            self.tokens[item] = self.tokens[item] + 1

    def __repr__(self):
        return f"{self.true_class} {self.tokens}"


# return the distance between two documents
def euclidean_distance(d1, d2) :
    # take the union of the tokens in each document
    union = d1.tokens.keys() | d2.tokens.keys()
    dist = sum([(d1.tokens[item] - d2.tokens[item])**2 for item in union])
    return dist

## You implement this.
def cosine_similarity(d1,d2) :
    xx, xy, yy = 0, 0, 0
    union = d1.tokens.keys() | d2.tokens.keys()
    for token in union :
        x = d1.tokens[token]
        y = d2.tokens[token]
        xx += x * x
        yy += y * y
        xy += x * y
        if xx == 0 or yy == 0:
            return 0
    return xy / sqrt(xx * yy)


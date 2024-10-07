## generate a simple dataset for clustering.
import random
import string

pos_lexicon = ['cat','dog','fish','monkey','goat','hippo','orangutan','whale','lobster','horse']
neg_lexicon = ['cat','fish','joke','map','right','fly', 'sled','tiger','hide','float']

def create_docs(npos, nneg) :
    length = 100
    stopwords = ['a', 'an', 'the']
    pos_docs = []
    neg_docs = []
    for i in range(npos) :
        if random.random() < 0.2:
            word = random.choice(stopwords)
        else:
            word = random.choice(pos_lexicon)
        if random.random() < 0.2:
            word = word.capitalize()
        if random.random() < 0.3:
            word += random.choice(string.punctuation)
        pos_docs.append(word)

    for j in range(nneg) :
        if random.random() < 0.2:
            word = random.choice(stopwords)
        else:
            word = random.choice(pos_lexicon)
        if random.random() < 0.2:
            word = word.capitalize()
        if random.random() < 0.3:
            word += random.choice(string.punctuation)
        neg_docs.append(word)

    return (pos_docs, neg_docs)
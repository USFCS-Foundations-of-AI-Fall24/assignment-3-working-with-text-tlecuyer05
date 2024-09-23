## generate a simple dataset for clustering.
import random

pos_lexicon = ['cat','dog','fish','monkey','goat','hippo','orangutan','whale','lobster','horse']
neg_lexicon = ['cat','fish','joke','map','right','fly', 'sled','tiger','hide','float']

def create_docs(npos, nneg) :
    length = 100
    pos_docs = []
    neg_docs = []
    for i in range(npos) :
        d = [random.choice(pos_lexicon) for j in range(length)]
        pos_docs.append(d)
    for j in range(nneg) :
        d = [random.choice(neg_lexicon) for j in range(length)]
        neg_docs.append(d)

    return (pos_docs, neg_docs)
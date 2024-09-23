from Cluster import *
from Document import *

def classify(clusters, item) :
    dist = 10000
    best = None
    for c in clusters :
        d = cosine_similarity(c.centroid, item)
        if d < dist :
            dist = d
            best = c
    return best.centroid.true_class


def five_fold_cross_validation(nwords, nelements) :
    pass
    ## generate nelements documents of each type (pos and neg), with nwords words in each doc.
    # divide the documents into 5 folds.
    ## for i = 1 to 5
    # cluster 80% of the documents. (four folds)
    #    use classify to classify the other 20%.
    #    measure accuracy - how many of the documents were classified correctly?
    # return the average accuracy



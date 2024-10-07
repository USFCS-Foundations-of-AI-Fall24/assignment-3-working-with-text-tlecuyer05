## Code for loading training sets and creating documents.
import string

from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])
def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        ## deal with filters here
        for f in filters:
            words = [word for word in words if f(word)]

        ## deal with transforms here
        for t in transforms:
            words = [t(word) for word in words]
        d.add_tokens(words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

# you do this.
def not_stopword(token) :
    return token not in ['a', 'an', 'the']

def not_cat(token) :
    return token != 'cat'


# transforms - convert a token into a new format

# you do this.
def remove_trailing_punct(token) :
    return token.rstrip(string.punctuation)

# and this
def convert_to_lowercase(token) :
    return token.lower()



## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes) :
    # hlist will be the homogeneity for each cluster.
    hlist = []
    for cluster in list_of_clusters:
        counts = [0] * len(list_of_classes)

        for doc in cluster.members:
            for i in range(len(list_of_classes)):
                if doc.true_class == list_of_classes[i]:
                    counts[i] += 1

        maxIdx = max(counts)
        totalDocs = len(cluster.members)
        if totalDocs > 0:
            homogeneity = maxIdx / totalDocs
        else:
            homogeneity = 0
        hlist.append(homogeneity)
    return hlist

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])

def compute_completeness(list_of_clusters, list_of_classes):
    # clist will be the homogeneity for each cluster.
    clist = []
    # Get the total counts of each class for every cluster
    total_counts = [0] * len(list_of_classes)
    for cluster in list_of_clusters:
        for doc in cluster.members:
            for i in range(len(list_of_classes)):
                if doc.true_class == list_of_classes[i]:
                    total_counts[i] += 1

    # Calculate the completeness for each cluster
    for cluster in list_of_clusters:
        counts = [0] * len(list_of_classes)
        for doc in cluster.members:
            for i in range(len(list_of_classes)):
                if doc.true_class == list_of_classes[i]:
                    counts[i] += 1

        majority_class_idx = counts.index(max(counts))
        majority_class = counts[majority_class_idx]
        total_majority_class = total_counts[majority_class_idx]
        if total_majority_class > 0:
            completeness_score = majority_class / total_majority_class
        else:
            completeness_score = 0

        clist.append(completeness_score)

    return clist

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(10,10)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])






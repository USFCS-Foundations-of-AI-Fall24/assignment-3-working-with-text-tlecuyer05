from Cluster import *
from Document import *
from Loader import *
from make_dataset import *
import argparse

def classify(clusters, item):
    dist = 10000
    best = None
    for c in clusters:
        d = cosine_similarity(c.centroid, item)
        if d < dist:
            dist = d
            best = c
    return best.centroid.true_class


def five_fold_cross_validation(nwords, nelements):
    all_docs = []
    ## generate nelements documents of each type (pos and neg), with nwords words in each doc.
    for _ in range(nelements):
        pos_reviews, neg_reviews = create_docs(nelements, nelements)
        positive_docs = create_easy_documents(pos_reviews, 'pos',
                                            filters=[not_stopword],
                                            transforms=[convert_to_lowercase, remove_trailing_punct])
        negative_docs = create_easy_documents(neg_reviews, 'neg',
                                            filters=[not_stopword],
                                            transforms=[convert_to_lowercase, remove_trailing_punct])
        all_docs.append(positive_docs[0])
        all_docs.append(negative_docs[0])

    # Shuffle the documents before folding
    random.shuffle(all_docs)

    all_accuracies = []

    # divide the documents into 5 folds.
    size = len(all_docs)//5
    folds = []
    for i in range(5):
        folds.append(all_docs[(i * size): ((i + 1) * size)])
    ## for i = 1 to 5
    for i in range(5):
        test_set = folds[i]
        # cluster 80% of the documents. (four folds)
        train_set = [doc for j in range(5) if j != i for doc in folds[j]]
        result = k_means(2, ['pos', 'neg'], train_set)
        num_correct = 0
        #    use classify to classify the other 20%.
        for doc in test_set:
            classification = classify(result, doc)
            if classification == doc.true_class:
                num_correct += 1
        #    measure accuracy - how many of the documents were classified correctly?
        all_accuracies.append((num_correct/len(test_set)))

    # return the average accuracy
    average_accuracy = sum(all_accuracies) / len(all_accuracies)
    return average_accuracy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Classifier',
        description='Classify pos/neg reviews using k-means'
    )
    parser.add_argument('-w', '--words', type=int, help='Number of words per document')
    parser.add_argument('-e', '--elements', type=int, help='Number of documents per class')
    args = parser.parse_args()
    average_accuracy = five_fold_cross_validation(args.words, args.elements)
    print(f'Average accuracy: {average_accuracy}')

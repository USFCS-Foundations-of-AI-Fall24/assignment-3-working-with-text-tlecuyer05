from pandasExercise import *
from Document import *
from Cluster import *
from Classifier import *
from Loader import *
from make_dataset import *
from test_Document import *

# Run everything for Problem #1, pandas
# Problem 1, Part 1
chapter1('breast-cancer.data')

# Problem 1, Part 2
chapter2('breast-cancer.data')

# Problem 1, Part 3
chapter3('breast-cancer.data')

# Problem 1, Part 4
chapter4('breast-cancer.data')

# Problem #2, Documents
# Problem 2, Part 1 (cosine similarity)
d = Document(true_class='pos')
d.add_tokens(['cat', 'dog', 'fish'])
d2 = Document(true_class='pos')
d2.add_tokens(['cat', 'dog'])
print(cosine_similarity(d, d2), "\n")

# Problem 2, Part 2 (centroids)
d = Document(true_class='pos')
d.add_tokens(['cat', 'dog', 'fish'])
d2 = Document(true_class='neg')
d2.add_tokens(['bunny', 'fish', 'octopus'])
d3 = Document(true_class='neg')
d3.add_tokens(['lizard', 'octopus', 'fish'])
doc_cluster = Cluster(members=[d, d2, d3])
Cluster.calculate_centroid(doc_cluster)
print(doc_cluster.centroid)

# Problem 2, Part 3 (kmeans)
# (Test in test_cluster uses document generator)
d = Document(true_class='pos')
d.add_tokens(['cat', 'dog', 'fish'])
d2 = Document(true_class='pos')
d2.add_tokens(['cat', 'dog', 'fish'])
d3 = Document(true_class='neg')
d3.add_tokens(['bunny', 'lizard', 'octopus'])
print(k_means(2, ['pos', 'neg'], [d, d2, d3]))

# problem 2, Part 4 (Homogeneity and completeness)
pos_reviews, neg_reviews = create_docs(10, 10)

positive_docs = create_easy_documents(pos_reviews, 'pos',
                                      filters=[],
                                      transforms=[])

negative_docs = create_easy_documents(neg_reviews, 'neg',
                                      filters=[],
                                      transforms=[])

result = k_means(2, ['pos', 'neg'], positive_docs + negative_docs)
res2 = compute_homogeneity(result, ['pos', 'neg'])
print("Homogeinity", res2)
res3 = compute_completeness(result, ['pos', 'neg'])
print("Completeness", res3)

# Problem 2, Part 5, 6 are in assignment3.pdf

# Problem 2, Part 7 (Implmenting filters and transforms)
pos_reviews, neg_reviews = create_docs(10, 10)

positive_docs = create_easy_documents(pos_reviews, 'pos',
                                      filters=[not_cat, not_stopword],
                                      transforms=[convert_to_lowercase, remove_trailing_punct])

negative_docs = create_easy_documents(neg_reviews, 'neg',
                                      filters=[not_cat, not_stopword],
                                      transforms=[convert_to_lowercase, remove_trailing_punct])
print(positive_docs, negative_docs)

# Problem 2, Part 8 (five-fold cross-validation)
# Main with command line is in Classifier.py
best_avg = 0.0
for i in range(100):
    avg = five_fold_cross_validation(5, 5)
    if avg > best_avg:
        best_avg = avg
print(f"The best 5-fold cross validation average after 100 trials is: {best_avg}")
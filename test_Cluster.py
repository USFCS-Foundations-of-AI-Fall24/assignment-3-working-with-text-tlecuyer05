from unittest import TestCase
from Cluster import *
from Document import *
from make_dataset import *

class TestCluster(TestCase):
    def test_calculate_centroid(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='neg')
        d2.add_tokens(['bunny', 'fish', 'octopus'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['lizard', 'octopus', 'fish'])
        doc_cluster = Cluster(members=[d, d2, d3])
        Cluster.calculate_centroid(doc_cluster)
        self.assertAlmostEqual(doc_cluster.centroid.tokens['fish'], 1)
        self.assertAlmostEqual(doc_cluster.centroid.tokens['cat'], 1 / 3)
        self.assertAlmostEqual(doc_cluster.centroid.tokens['dog'], 1 / 3)
        self.assertAlmostEqual(doc_cluster.centroid.tokens['bunny'], 1 / 3)
        self.assertAlmostEqual(doc_cluster.centroid.tokens['octopus'], 2 / 3)
        self.assertAlmostEqual(doc_cluster.centroid.tokens['lizard'], 1 / 3)

    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        print(k_means(2, ['pos', 'neg'], [d, d2, d3]))

        # Using documents generator
        pos_docs, neg_docs = create_docs(2, 1)
        all_docs = []
        for doc in pos_docs:
            d = Document(true_class='pos')
            d.add_tokens(doc)
            all_docs.append(d)
        for doc in neg_docs:
            d = Document(true_class='neg')
            d.add_tokens(doc)
            all_docs.append(d)
        print(k_means(2, ['pos', 'neg'], all_docs))



from unittest import TestCase
from Cluster import *
from Document import *

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
        print(doc_cluster)
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
        print(k_means(2, ['pos', 'neg'], [d,d2,d3]))



from unittest import TestCase
from Loader import *


class Test(TestCase):
    def test_apply_filters(self):
        pass

    def test_apply_transforms(self):
        pass

    def test_workflow(self):
        pos_reviews, neg_reviews = create_docs(10, 10)

        positive_docs = create_easy_documents(pos_reviews, 'pos',
                                              filters=[],
                                              transforms=[])

        negative_docs = create_easy_documents(neg_reviews, 'neg',
                                              filters=[],
                                              transforms=[])

        result = k_means(2, ['pos', 'neg'], positive_docs + negative_docs)
        res2 = compute_homogeneity(result, ['pos','neg'])
        print("Homogeinity", res2)
        res3 = compute_completeness(result, ['pos', 'neg'])
        print("Completeness", res3)




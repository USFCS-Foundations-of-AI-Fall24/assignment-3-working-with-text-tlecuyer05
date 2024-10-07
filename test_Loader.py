from unittest import TestCase
from Loader import *


class Test(TestCase):
    def test_apply_filters(self):
        tokens1 = ['a', 'cat', 'is']
        filtered1 = []
        for token in tokens1:
            if not_cat(token):
                filtered1.append(token)
        tokens2 = ['a', 'cat', 'is']
        filtered2 = []
        for token in tokens2:
            if not_stopword(token):
                filtered2.append(token)
        self.assertEqual(filtered1, ['a', 'is'])
        self.assertEqual(filtered2, ['cat', 'is'])

    def test_apply_transforms(self):
        tokens1 = ['a.', 'cat.', 'is.']
        filtered1 = []
        for token in tokens1:
            filtered1.append(remove_trailing_punct(token))
        tokens2 = ['A', 'CAT', 'IS']
        filtered2 = []
        for token in tokens2:
            if not_stopword(token):
                filtered2.append(convert_to_lowercase(token))
        self.assertEqual(filtered1, ['a', 'cat', 'is'])
        self.assertEqual(filtered2, ['a', 'cat', 'is'])

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




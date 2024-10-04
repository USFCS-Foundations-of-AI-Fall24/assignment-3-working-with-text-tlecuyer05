import random

from Document import *


class Cluster:
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid:
            self.centroid = centroid
        else:
            self.centroid = Document(true_class='pos')
        if members:
            self.members = members
        else:
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

    ## You do this.
    def calculate_centroid(self):
        self.centroid.tokens.clear()
        for doc in self.members:
            self.centroid.add_tokens(doc.tokens)
        for token in self.centroid.tokens:
            self.centroid.tokens[token] = self.centroid.tokens[token] / len(self.members)


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data):
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    random.shuffle(data)
    # Initially assign data to clusters randomly.
    for item in data:
        random_cluster_index = random.randint(0, n_clusters - 1)
        cluster_list[random_cluster_index].members.append(item)

    # compute initial cluster centroids
    for cluster in cluster_list:
        Cluster.calculate_centroid(cluster)

    done = False
    i = 0
    while i < 100 and not done:
        i += 1
        starting_centroids = [cluster.centroid.tokens.copy() for cluster in cluster_list]
        for cluster in cluster_list:
            cluster.members = []  # Clear the cluster document lists
        for doc in data:
            # Get a list of all similarities for each cluster
            all_similarities = [cosine_similarity(doc, cluster.centroid) for cluster in cluster_list]
            most_similar_cluster = all_similarities.index(max(all_similarities))
            #   reassign each Document to the closest matching cluster
            cluster_list[most_similar_cluster].members.append(doc)

        # Calculate new centroid
        for cluster in cluster_list:
            Cluster.calculate_centroid(cluster)

        for idx in range(len(cluster_list)):
            if cluster_list[idx].centroid.tokens != starting_centroids[idx]:
                break

        # Update done if nothing has changed
        done = True
    return cluster_list

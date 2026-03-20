import networkx as nx
import visualizer as viz
import experiments as exp
import csv

G = nx.Graph()


# we import the network
with open("Friendship-network_data_2013.csv") as f:
    reader = csv.reader(f)
    for s in reader:
        i = s[0].split()
        G.add_edge(i[0], i[1])

# we select the largest connected component
G = G.subgraph(max(nx.connected_components(G), key=len)).copy()


# We compute various centralities for each node and we order them from the
# most central to the least central according to every measure.
print("Centralities computation start!")
degree = sorted(
    nx.degree_centrality(G).items(),
    key=(
        lambda key: key[1]),
    reverse=True)
print("Degree Centrality Computed")
eigen = sorted(nx.eigenvector_centrality_numpy(G).items(),
               key=(lambda key: key[1]), reverse=True)
print("Eigenvector Centrality Computed")
betweeness = sorted(nx.betweenness_centrality(G).items(),
                    key=(lambda key: key[1]), reverse=True)
print("Betweenness Centrality Computed")
closeness = sorted(
    nx.closeness_centrality(G).items(),
    key=(
        lambda key: key[1]),
    reverse=True)
print("Closeness Centrality Computed")

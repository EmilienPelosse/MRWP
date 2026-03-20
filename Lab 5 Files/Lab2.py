import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# (a) Load network
G = nx.Graph()
with open('Data/Friendship-network_data_2013.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        G.add_edge(row[0], row[1])

# (b) Draw network
'''
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_size=300, font_size=7)
plt.title("Full Network")
plt.show()
'''

# (c) Spectral bisection function
def spectral_bisection(graph):
    # (d) Handle disconnected graph — work on giant component only
    if not nx.is_connected(graph):
        print("Graph is not connected — extracting giant component.")
        giant_nodes = max(nx.connected_components(graph), key=len)
        graph = graph.subgraph(giant_nodes)

    part_A, part_B = nx.spectral_bisection(graph)
    return part_A, part_B

# (d) Partition the network
connected_components = list(nx.connected_components(G))
giant_component_nodes = max(connected_components, key=len)
giant_component = G.subgraph(giant_component_nodes)

part_A, part_B = spectral_bisection(giant_component)

print(f"Partition A: {len(part_A)} nodes")
print(f"Partition B: {len(part_B)} nodes")

# (e) Draw network with communities highlighted
plt.figure(figsize=(10, 10))

pos = nx.spring_layout(giant_component, seed=42)

# Draw edges
nx.draw_networkx_edges(giant_component, pos, alpha=0.3, edge_color='gray')

# Draw each partition with a different color using draw_networkx_nodes
nx.draw_networkx_nodes(giant_component, pos,
                       nodelist=list(part_A),
                       node_color='steelblue',
                       node_size=300,
                       label='Community A')

nx.draw_networkx_nodes(giant_component, pos,
                       nodelist=list(part_B),
                       node_color='orange',
                       node_size=300,
                       label='Community B')

nx.draw_networkx_labels(giant_component, pos, font_size=7)

plt.title("Spectral Bisection — Two Communities")
plt.legend(scatterpoints=1)
plt.show()

# f) 

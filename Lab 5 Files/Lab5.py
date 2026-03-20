import networkx as nx
import engine as en
import visualizer as viz
import csv

# Create graph
G = nx.Graph()
with open('Friendship-network_data_2013.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        G.add_edge(row[0], row[1])


print(nx.spring_layout(G))
# Layout for visualization
positions = nx.spring_layout(G)

# Choose nodes
nodes = list(G.nodes())
groupA = nodes[:10]       # Dakota supporters
groupB = nodes[10:20]    # Opponent supporters

# Run simulation
data = en.graphModelRun(G, 100, groupA, groupB)

# Visualize
viz.showGraphDynamic(G, data, positions, "TEST")
viz.showData(data, "TEST")
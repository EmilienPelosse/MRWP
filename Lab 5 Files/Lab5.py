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

connected_components = list(nx.connected_components(G))
giant_component_nodes = max(connected_components, key=len)

giant_component = G.subgraph(giant_component_nodes)
print(giant_component)

print(nx.spring_layout(giant_component))
# Layout for visualization
positions = nx.spring_layout(giant_component)

# Choose nodes
nodes = list(giant_component.nodes())
groupA = nodes[:10]       # Dakota supporters
groupB = nodes[10:20]    # Opponent supporters

# Run simulation
data = en.graphModelRun(giant_component, 100, groupA, groupB)

# Visualize
viz.showGraphDynamic(giant_component, data, positions, "TEST")
viz.showData(data, "TEST")
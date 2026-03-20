import networkx as nx
import engine as en
import visualizer as viz


G=nx.grid_graph([50,50])

positions=dict(((i,j),(i,j)) for (i,j) in G.nodes())
nx.draw(G,pos=positions)

data=en.graphModelRun(G,100,[(25,25)],[(26,26)])
viz.showGraphDynamic(G,data,positions,"TEST")
viz.showData(data,"TEST")
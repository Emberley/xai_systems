import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue")
    plt.show()

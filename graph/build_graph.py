import networkx as nx

def build_graph():
    G = nx.Graph()

    # Add nodes
    G.add_node("U1", type="user")
    G.add_node("U2", type="user")

    G.add_node("I1", type="item")
    G.add_node("I2", type="item")

    # Add relationships
    G.add_edge("U1", "I1", relation="viewed")
    G.add_edge("U1", "I2", relation="liked")
    G.add_edge("U2", "I2", relation="viewed")

    return G
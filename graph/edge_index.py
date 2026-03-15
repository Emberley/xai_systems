import torch

def graph_to_edge_index(G):
    node_map = {n: i for i, n in enumerate(G.nodes())}
    edges = []

    for u, v in G.edges():
        edges.append([node_map[u], node_map[v]])
        edges.append([node_map[v], node_map[u]])

    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
    return edge_index, node_map

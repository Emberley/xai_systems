import torch

def create_node_features(graph):
    num_nodes = graph.number_of_nodes()
    return torch.eye(num_nodes)  # simple one-hot encoding

from torch_geometric.explain import GNNExplainer

def explain(model, x, edge_index, node_id):
    explainer = GNNExplainer(model, epochs=200)
    explanation = explainer.explain_node(node_id, x, edge_index)
    return explanation

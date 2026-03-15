from graph.build_graph import build_graph
from graph.edge_index import graph_to_edge_index
from models.gnn_model import GNN
from models.recommender import recommend
from explainability.path_reasoning import explain_path

# Knowledge Graph
G = build_graph()

# Convert graph to ML format
edge_index, node_map = graph_to_edge_index(G)

# Reverse mapping: index → node name
index_to_node = {idx: name for name, idx in node_map.items()}

# Initialize Model
model = GNN(num_nodes=len(node_map))

# Generate embeddings
embeddings = model(edge_index)

# Generate Recommendation
user_id = node_map["U1"]  # Change user here if needed

recommended_indices = recommend(user_id, embeddings)

recommended_nodes = [index_to_node[i.item()] for i in recommended_indices]

print("\nRecommendations:")
for i, node in enumerate(recommended_nodes, 1):
    print(f"{i}. {node} (type: {G.nodes[node]['type']})")

# Explain Recommendation Path
print("\nExplanation paths:")

for node in recommended_nodes:
    if G.nodes[node]["type"] == "item":
        path = explain_path(G, index_to_node[user_id], node)

        if path:
            relation_path = " -> ".join(path)
            print(f"{index_to_node[user_id]} -> {node}: {relation_path}")
        else:
            print(f"No path found from {index_to_node[user_id]} to {node}")

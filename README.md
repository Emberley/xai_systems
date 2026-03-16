# XAI System
**XAI Recommender System using a Graph Knowledge Base**

## Overview
This code implements a simple explainable recommender system built on a knowledge graph and a Graph Neural Network (GNN).The graph is converted and passed into a GNN to generate node embeddings. These embeddings are then used to recommend items for a user. The system includes an explainability component that identifies paths in the knowledge graph connecting the user to the recommended items.

## Methods
1. Build Knowledge Graph  Load nodes and edges into a graph `G`  
2. Convert the graph to `edge_index` for the GNN  
3. Train or compute node embeddings  
4. Generate recommended items for a user  
5. Compute paths in the graph 
6. Draw the graph 
7. Assess recommendation quality using metrics like `precision@k`  

---

## Technologies
- Python  
- NumPy & Pandas  
- PyTorch / PyTorch Geometric
- NetworkX & Matplotlib 

---

## Usage
Clone the repository and run the analysis:

```bash
# Clone repository
git clone https://github.com/Emberley/xai_systems.git

# Install dependencies
pip install -r requirements.txt



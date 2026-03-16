# XAI Systems

## Overview


---

## System Workflow
1. **Build Knowledge Graph** – Load nodes and edges into a graph `G`  
2. **Graph → ML Format** – Convert the graph to `edge_index` for the GNN  
3. **GNN Embeddings** – Train or compute node embeddings  
4. **Recommendations** – Generate recommended items for a user  
5. **Explanation** – Compute paths in the graph 
6. **Visualization** – Draw the graph 
7. **Evaluation** – Assess recommendation quality using metrics like `precision@k`  

---

## Technologies
- Python  
- NumPy & Pandas  
- PyTorch / PyTorch Geometric (for GNNs)  
- NetworkX & Matplotlib (graph visualization)  

---

## Usage
Clone the repository and run the analysis:

```bash
# Clone repository
git clone https://github.com/Emberley/xai_systems.git

# Install dependencies
pip install -r requirements.txt

# Run main analysis to generate embeddings and recommendations
python analysis/run_analysis.py

# Visualize the knowledge graph
python visualization/plot_results.py

# XAI Systems

## Overview
**xai_systems** is a modular framework for **Explainable Artificial Intelligence (XAI)** that combines **knowledge graphs, graph neural networks (GNNs), recommendations, explainability, visualization, and evaluation**.  

The system helps analyze and interpret machine learning predictions by:  
- Generating embeddings for nodes in a knowledge graph  
- Making personalized recommendations  
- Explaining recommendations via paths in the graph  
- Visualizing graph structures  
- Evaluating recommendation performance  

This project reduces the “black-box” nature of ML systems by providing interpretable outputs and visual explanations.

---

## Key Features
- Build and manipulate **knowledge graphs** of users/items  
- Train **Graph Neural Networks (GNNs)** to generate node embeddings  
- Make **recommendations** for users based on learned embeddings  
- Explain recommendations via **graph path reasoning**  
- Visualize knowledge graphs using **NetworkX + Matplotlib**  
- Evaluate recommendations with metrics like **precision@k**

---

## System Workflow
1. **Build Knowledge Graph** – Load nodes and edges into a graph `G`  
2. **Graph → ML Format** – Convert the graph to `edge_index` for the GNN  
3. **GNN Embeddings** – Train or compute node embeddings  
4. **Recommendations** – Generate recommended items for a user  
5. **Explanation** – Compute paths in the graph showing how recommendations are derived  
6. **Visualization** – Draw the graph for better interpretability  
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

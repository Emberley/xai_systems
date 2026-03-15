import torch

def recommend(user_id, embeddings, top_k=3):
    user_vec = embeddings[user_id]
    scores = torch.matmul(embeddings, user_vec)
    return torch.topk(scores, top_k).indices

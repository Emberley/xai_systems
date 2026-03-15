import numpy as np

def precision_at_k(recommended, ground_truth, k=3):
    recs = set(recommended[:k])
    truth = set(ground_truth)
    return len(recs & truth) / k

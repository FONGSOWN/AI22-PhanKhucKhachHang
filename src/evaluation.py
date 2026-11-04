"""Khảo sát Elbow và Silhouette cho các K hợp lệ."""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from .clustering import _features

def evaluate_k_range(rfm, max_k=8):
    scaled = _features(rfm); upper = min(max_k, len(rfm)-1)
    if upper < 2: raise ValueError("Không đủ khách hàng để khảo sát K.")
    rows=[]
    for k in range(2, upper+1):
        model = KMeans(n_clusters=k, random_state=42, n_init=20).fit(scaled)
        rows.append({"K": k, "Inertia": model.inertia_, "Silhouette": silhouette_score(scaled, model.labels_)})
    return pd.DataFrame(rows)

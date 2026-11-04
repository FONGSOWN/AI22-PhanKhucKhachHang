"""Huấn luyện K-Means trên RFM đã chuẩn hóa."""
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
FEATURES = ["Recency", "Frequency", "Monetary"]

def _features(rfm):
    if len(rfm) < 3: raise ValueError("Cần ít nhất 3 khách hàng để phân cụm.")
    if rfm[FEATURES].isna().any().any(): raise ValueError("RFM có giá trị thiếu.")
    return StandardScaler().fit_transform(rfm[FEATURES])

def cluster_customers(rfm, k):
    if not 2 <= k < len(rfm): raise ValueError(f"K phải từ 2 đến {len(rfm)-1}.")
    scaled = _features(rfm); model = KMeans(n_clusters=k, random_state=42, n_init=20); labels = model.fit_predict(scaled)
    result = rfm.copy(); result["Cluster"] = labels
    return result, float(silhouette_score(scaled, labels)), float(model.inertia_)

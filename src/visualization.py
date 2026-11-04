"""Biểu đồ cho giao diện."""
import matplotlib.pyplot as plt
import seaborn as sns
def plot_evaluation(scores):
    fig, axes = plt.subplots(1,2,figsize=(12,4)); axes[0].plot(scores.K,scores.Inertia,marker="o"); axes[0].set(title="Elbow Method",xlabel="K",ylabel="Inertia (SSE)"); axes[1].plot(scores.K,scores.Silhouette,marker="o",color="#0e7490"); axes[1].set(title="Silhouette Score",xlabel="K",ylabel="Điểm silhouette"); fig.tight_layout(); return fig
def plot_segments(result):
    fig, ax=plt.subplots(figsize=(8,5)); sns.scatterplot(data=result,x="Frequency",y="Monetary",hue="Cluster",palette="Set2",s=80,ax=ax); ax.set_title("Frequency – Monetary theo cụm"); return fig

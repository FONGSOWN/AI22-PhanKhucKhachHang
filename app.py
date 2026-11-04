import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_processing import clean_transactions
from src.rfm import build_rfm
from src.clustering import cluster_customers
from src.evaluation import evaluate_k_range
from src.visualization import plot_evaluation, plot_segments

st.set_page_config(page_title="AI22 | Phân khúc khách hàng", page_icon="📊", layout="wide")
st.title("📊 Phân khúc khách hàng thương mại điện tử")
st.caption("Đồ án Trí tuệ nhân tạo #22 · RFM + K-Means · Kết quả tính trực tiếp từ dữ liệu")

def summarize_segments(result):
    total=len(result); avg=result[["Recency","Frequency","Monetary"]].mean()
    summary=result.groupby("Cluster",as_index=False).agg(**{"Số khách hàng":("CustomerID","count"),"Recency TB":("Recency","mean"),"Frequency TB":("Frequency","mean"),"Monetary TB":("Monetary","mean"),"Tổng doanh thu":("Monetary","sum")})
    summary["Tỷ lệ (%)"]=summary["Số khách hàng"]/total*100
    def label(r):
        if r["Recency TB"]<=avg.Recency and r["Frequency TB"]>=avg.Frequency and r["Monetary TB"]>=avg.Monetary: return "Giá trị cao"
        if r["Recency TB"]<=avg.Recency and r["Frequency TB"]>=avg.Frequency: return "Trung thành / hoạt động"
        if r["Recency TB"]>avg.Recency and r["Monetary TB"]>=avg.Monetary: return "Có nguy cơ rời bỏ"
        return "Ít hoạt động"
    summary["Diễn giải"]=summary.apply(label,axis=1); return summary.round(2)

with st.sidebar:
    st.header("Dữ liệu & mô hình")
    uploaded=st.file_uploader("Tải CSV giao dịch",type="csv")
    st.caption("Cột cần có: CustomerID, InvoiceDate, InvoiceNo, Quantity, UnitPrice")
raw=pd.read_csv(uploaded) if uploaded else pd.read_csv("data/sample_transactions.csv")
if not uploaded: st.info("Đang dùng dữ liệu mẫu; tải CSV riêng ở thanh bên.")
try:
    cleaned,report=clean_transactions(raw); rfm=build_rfm(cleaned); scores=evaluate_k_range(rfm)
    with st.sidebar: k=st.selectbox("Chọn số cụm K",scores.K.tolist(),index=int(scores.Silhouette.idxmax()))
    result,silhouette,inertia=cluster_customers(rfm,k); summary=summarize_segments(result)
except Exception as error:
    st.error(f"Không thể phân tích dữ liệu: {error}"); st.stop()

tab1,tab2,tab3,tab4,tab5=st.tabs(["Tổng quan","Dữ liệu","Phân tích RFM","Mô hình AI","Kết quả & xuất"])
with tab1:
    a,b,c,d=st.columns(4); a.metric("Giao dịch hợp lệ",len(cleaned)); b.metric("Khách hàng",len(rfm)); c.metric("Doanh thu",f"{cleaned.Revenue.sum():,.2f}"); d.metric("K đã chọn",k)
    st.subheader("Quy trình"); st.write("CSV → làm sạch → RFM → StandardScaler → K-Means → đánh giá và diễn giải cụm.")
    st.caption("Recency: số ngày từ lần mua gần nhất; Frequency: số hóa đơn khác nhau; Monetary: tổng chi tiêu.")
with tab2:
    st.subheader("Xem trước dữ liệu gốc"); st.dataframe(raw.head(20),use_container_width=True)
    st.subheader("Báo cáo tiền xử lý"); st.dataframe(pd.DataFrame(report.items(),columns=["Quy tắc","Số dòng"]),use_container_width=True)
    st.caption("Bỏ dòng thiếu/sai kiểu, hóa đơn bắt đầu C, Quantity ≤ 0 hoặc UnitPrice < 0. Giá bằng 0 được giữ; không tự loại ngoại lệ doanh thu lớn.")
with tab3:
    st.subheader("Bảng RFM"); st.dataframe(rfm,use_container_width=True)
    fig,axes=plt.subplots(1,3,figsize=(13,3))
    for ax,col in zip(axes,["Recency","Frequency","Monetary"]): sns.histplot(rfm[col],kde=True,ax=ax); ax.set_title(col)
    st.pyplot(fig)
with tab4:
    st.subheader("Lựa chọn K"); st.pyplot(plot_evaluation(scores)); st.dataframe(scores.round(3),use_container_width=True)
    st.info("Ưu tiên K có Silhouette cao (gần 1 tốt hơn) và điểm gãy Elbow hợp lý. K cuối cùng do người dùng chọn, không cố định.")
    x,y=st.columns(2); x.metric("Silhouette của K đã chọn",f"{silhouette:.3f}"); y.metric("Inertia (SSE)",f"{inertia:.3f}")
with tab5:
    st.subheader("Tóm tắt phân khúc"); st.dataframe(summary,use_container_width=True)
    st.caption("Nhãn được diễn giải tương đối theo trung bình toàn bộ dữ liệu, không phải nhãn sẵn có của thuật toán.")
    st.pyplot(plot_segments(result))
    selected=st.multiselect("Lọc theo cụm",sorted(result.Cluster.unique()),default=sorted(result.Cluster.unique()))
    st.dataframe(result[result.Cluster.isin(selected)],use_container_width=True)
    left,right=st.columns(2)
    left.download_button("Tải khách hàng đã phân cụm",result.to_csv(index=False).encode("utf-8-sig"),"rfm_segments.csv","text/csv")
    right.download_button("Tải tổng hợp phân khúc",summary.to_csv(index=False).encode("utf-8-sig"),"segment_summary.csv","text/csv")

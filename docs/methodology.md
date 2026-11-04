# Cơ sở lý thuyết RFM và K-Means

Phân cụm khách hàng là học **không giám sát**: không có nhãn “VIP” hoặc “rời bỏ” cho mô hình học trước. RFM tóm tắt hành vi bằng Recency (mới mua cách đây bao lâu), Frequency (số hóa đơn) và Monetary (tổng chi tiêu).

Với ngày tham chiếu `T`: `R_i = T - max(ngày mua_i)`, `F_i = số InvoiceNo khác nhau`, `M_i = tổng(Quantity × UnitPrice)`. App dùng ngày sau giao dịch muộn nhất làm `T`.

K-Means lặp việc gán điểm vào tâm gần nhất và cập nhật tâm bằng trung bình cụm. Nó tối thiểu hóa `J = Σ(k=1..K) Σ(x_i thuộc C_k) ||x_i - μ_k||²`. StandardScaler cần thiết vì ba biến có đơn vị khác nhau. `random_state=42`, `n_init=20` giúp tái lập kết quả.

Elbow biểu diễn Inertia/SSE theo K để tìm điểm gãy; Silhouette `s=(b-a)/max(a,b)` so sánh khoảng cách trong cụm `a` và cụm gần nhất `b`. Điểm gần 1 tốt hơn. Chọn K cần kết hợp hai biểu đồ và ý nghĩa kinh doanh, không cố định 3 hay 4.

K-Means nhanh, dễ giải thích nhưng nhạy với K, ngoại lệ, thang đo và phù hợp nhất với cụm gần hình cầu. RFM chưa phản ánh lợi nhuận, danh mục, kênh mua hay nhân khẩu học; nhãn app chỉ là diễn giải tương đối theo dữ liệu hiện tại.

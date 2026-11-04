# BÁO CÁO ĐỒ ÁN: Phân khúc khách hàng thương mại điện tử bằng RFM và K-Means

## 1. Trang bìa
Điền tên trường, học phần, giảng viên, nhóm thực hiện, lớp và năm học.

## 2–3. Lời mở đầu, mục tiêu và phạm vi
Xây dựng ứng dụng phân cụm khách hàng từ giao dịch. Phạm vi là RFM và K-Means, không dự báo rời bỏ.

## 4–6. Cơ sở lý thuyết, phân tích, phương pháp
Trình bày theo `docs/methodology.md`, kèm luồng CSV → làm sạch → RFM → chuẩn hóa → K-Means → đánh giá.

## 7–8. Thiết kế và cài đặt
Mô tả các mô-đun `src/`, Streamlit, quy tắc tiền xử lý, `random_state=42`, `n_init=20`.

## 9–10. Thực nghiệm và đánh giá
Chỉ thêm bảng K, Silhouette, Inertia, khách hàng/cụm và ảnh biểu đồ sau khi chạy trên dataset đã chọn. Dữ liệu mẫu hiện tại chỉ là demo, không phải kết quả tổng quát.

## 11–13. Hạn chế, kết luận, tài liệu tham khảo
Nêu hạn chế RFM/K-Means; hướng phát triển: thêm lợi nhuận/kênh mua, xử lý ngoại lệ có kiểm soát, so sánh GMM/DBSCAN. Tham khảo scikit-learn User Guide và Fader, Hardie & Lee (2005).

# AI22 — Phân khúc khách hàng thương mại điện tử

Ứng dụng Streamlit áp dụng RFM và K-Means để phân nhóm khách hàng từ dữ liệu giao dịch. Đây là bài toán học **không giám sát**: không cần cột nhãn có trước.

## Chạy trên Windows

Mở thư mục `D:\AI22_PhanKhucKhachHang` trong VS Code, mở Terminal PowerShell và chạy lần lượt:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest
streamlit run app.py
```

Nếu PowerShell chặn kích hoạt, chạy `Set-ExecutionPolicy -Scope Process Bypass`, rồi kích hoạt lại.

## Định dạng CSV

Cần năm cột: `CustomerID`, `InvoiceDate`, `InvoiceNo`, `Quantity`, `UnitPrice`. Ứng dụng loại dòng thiếu/sai định dạng, hóa đơn bắt đầu `C`, số lượng không dương và giá âm. Giá bằng 0 được giữ và báo cáo; ngoại lệ doanh thu lớn không bị tự loại.

## Cấu trúc

- `src/`: làm sạch, RFM, K-Means, đánh giá và biểu đồ.
- `data/sample_transactions.csv`: dữ liệu minh họa, không phải kết quả thực nghiệm đại diện.
- `tests/`: kiểm thử các quy tắc quan trọng.
- `docs/`: cơ sở lý thuyết, khung báo cáo và kịch bản demo.

"""Tạo các chỉ số RFM từ giao dịch đã được làm sạch."""
import pandas as pd


def build_rfm(data: pd.DataFrame, reference_date=None) -> pd.DataFrame:
    """Tính Recency, Frequency, Monetary; ngày tham chiếu mặc định là ngày sau giao dịch cuối."""
    required = ["CustomerID", "InvoiceDate", "InvoiceNo", "Quantity", "UnitPrice"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError("Thiếu cột bắt buộc: " + ", ".join(missing))
    if data.empty:
        raise ValueError("Dữ liệu giao dịch đang rỗng.")
    df = data.copy()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    if df["InvoiceDate"].isna().any():
        raise ValueError("InvoiceDate có giá trị ngày không hợp lệ; hãy làm sạch trước.")
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    snapshot = pd.Timestamp(reference_date) if reference_date else df["InvoiceDate"].max() + pd.Timedelta(days=1)
    if snapshot <= df["InvoiceDate"].max():
        raise ValueError("Ngày tham chiếu phải sau ngày giao dịch muộn nhất.")
    rfm = df.groupby("CustomerID", as_index=False).agg(
        Recency=("InvoiceDate", lambda dates: (snapshot - dates.max()).days),
        Frequency=("InvoiceNo", "nunique"), Monetary=("Revenue", "sum"),
    )
    if (rfm[["Recency", "Frequency", "Monetary"]] < 0).any().any():
        raise ValueError("RFM chứa giá trị âm không hợp lệ.")
    return rfm.sort_values("Monetary", ascending=False).reset_index(drop=True)

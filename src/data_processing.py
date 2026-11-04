"""Đọc, kiểm tra và làm sạch dữ liệu giao dịch."""
import pandas as pd
REQUIRED_COLUMNS = ["CustomerID", "InvoiceDate", "InvoiceNo", "Quantity", "UnitPrice"]

def validate_columns(data):
    missing = [c for c in REQUIRED_COLUMNS if c not in data.columns]
    if missing: raise ValueError("CSV thiếu cột bắt buộc: " + ", ".join(missing))
    if data.empty: raise ValueError("CSV không có dòng dữ liệu.")

def clean_transactions(data):
    """Bỏ thiếu/sai định dạng, hóa đơn hủy, Quantity<=0 hoặc UnitPrice<0; giữ giá 0."""
    validate_columns(data); df = data.copy(); report = {"Trước làm sạch": len(df)}
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    for c in ["Quantity", "UnitPrice"]: df[c] = pd.to_numeric(df[c], errors="coerce")
    bad = df[REQUIRED_COLUMNS].isna().any(axis=1) | df["CustomerID"].astype(str).str.strip().eq("") | df["InvoiceNo"].astype(str).str.strip().eq("")
    report["Bỏ thiếu/sai định dạng"] = int(bad.sum()); df = df.loc[~bad].copy()
    cancelled = df["InvoiceNo"].astype(str).str.strip().str.upper().str.startswith("C"); report["Bỏ hóa đơn hủy"] = int(cancelled.sum()); df = df.loc[~cancelled].copy()
    invalid = (df["Quantity"] <= 0) | (df["UnitPrice"] < 0); report["Bỏ số lượng/giá không hợp lệ"] = int(invalid.sum()); df = df.loc[~invalid].copy()
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]; report["Sau làm sạch"] = len(df); report["Giá bằng 0 được giữ"] = int((df["UnitPrice"] == 0).sum())
    if df.empty: raise ValueError("Không còn giao dịch hợp lệ sau làm sạch.")
    return df.reset_index(drop=True), report

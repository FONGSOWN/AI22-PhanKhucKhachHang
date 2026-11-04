import pandas as pd
import pytest
from src.data_processing import clean_transactions, validate_columns
def test_clean_removes_invalid_rows():
    df=pd.DataFrame({"CustomerID":["A","B","C"],"InvoiceDate":["2025-01-01"]*3,"InvoiceNo":["1","C2","3"],"Quantity":[1,1,-1],"UnitPrice":[10,10,10]})
    cleaned,report=clean_transactions(df); assert len(cleaned)==1 and report["Bỏ hóa đơn hủy"]==1
def test_missing_columns():
    with pytest.raises(ValueError): validate_columns(pd.DataFrame({"CustomerID":["A"]}))

import pandas as pd
from src.rfm import build_rfm
def test_rfm_counts_unique_invoice_and_revenue():
    df=pd.DataFrame({"CustomerID":["A","A","B"],"InvoiceDate":["2025-01-01","2025-01-01","2025-01-02"],"InvoiceNo":["I1","I1","I2"],"Quantity":[2,1,1],"UnitPrice":[10,10,20]})
    r=build_rfm(df,"2025-01-03").set_index("CustomerID"); assert r.loc["A","Frequency"]==1 and r.loc["A","Monetary"]==30

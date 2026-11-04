import pandas as pd
import pytest
from src.clustering import cluster_customers
def test_cluster_returns_labels():
    rfm=pd.DataFrame({"CustomerID":list("ABCD"),"Recency":[1,2,30,31],"Frequency":[10,9,1,1],"Monetary":[100,90,10,12]})
    out,score,_=cluster_customers(rfm,2); assert "Cluster" in out and -1<=score<=1
def test_invalid_k():
    rfm=pd.DataFrame({"CustomerID":list("ABC"),"Recency":[1,2,3],"Frequency":[1,2,3],"Monetary":[1,2,3]})
    with pytest.raises(ValueError): cluster_customers(rfm,3)

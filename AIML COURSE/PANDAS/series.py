# series is a lable column 
# 1 dimension 
import pandas as pd

data=[100,200,300,400]

s=pd.Series(data,["one","two","three","four"])
# loc means location 
print(s.loc["two"])
# i loc is used for index based 
print(s.iloc[0])
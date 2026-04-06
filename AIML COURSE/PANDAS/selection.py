import pandas as pd

csv=pd.read_csv("data.csv",index_col="First Name")
# selection by column 
print(csv["Last Name"])

print(".........................................")
# multiple columns selection 
print(csv[["Last Name","Sex"]].to_string())

# selection by row
print("...................................")
print(csv.loc["Dennis"])

print("...................................")
# selection rows by slicing 

print(csv.iloc[0:5,0:5])

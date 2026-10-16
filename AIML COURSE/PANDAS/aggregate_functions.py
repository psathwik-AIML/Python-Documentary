import pandas as pd

csv_data=pd.read_csv("data.csv")

print(csv_data.to_string())

print("...................................")

# aggregate functions on dataframe 
print(f"sum: {csv_data.sum(numeric_only=True)}")
print(f"mean: {csv_data.mean(numeric_only=True)}")
print(f"count: {csv_data.count()}")
print(f"min: {csv_data.min(numeric_only=True)}")
print(f"max: {csv_data.max(numeric_only=True)}")

print(".........................")
# aggregate functions on single column
print(f"sum: {csv_data['Index'].sum()}")
print(f"mean: {csv_data['Index'].mean()}")
print(f"count: {csv_data['Index'].count()}")
print(f"min: {csv_data['Index'].min()}")
print(f"max: {csv_data['Index'].max()}")

print(".........................")
# group by function 

small_data=pd.read_csv("smalldata.csv")
print(small_data.to_string())

group=small_data.groupby("Sex")
print(group["Index"].sum())
print(group["Index"].mean())
print(group["Index"].min())
print(group["Index"].max())
print(group["Index"].count())
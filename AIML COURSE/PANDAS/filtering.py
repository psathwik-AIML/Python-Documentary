import pandas as pd 

data=pd.read_csv("data.csv")
# all data 

print(data.to_string())
print("..................................")

# filtering based on gender
males=data[data["Sex"]=="Male"]
print(males.to_string())
# females 
print("..................................")
females=data[data["Sex"]=="Female"]
print(females.to_string())

# multiple conditions 
print("................................")
m=data[(data["Index"]==1)  | (data["Index"]==10)]
print(m.to_string())

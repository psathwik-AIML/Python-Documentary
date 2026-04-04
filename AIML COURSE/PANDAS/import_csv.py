# importing csv file 

import pandas as pd

data=pd.read_csv("data.csv")

# prints some rows and columns 
print(data)

print("........................................")
# prints all data 
print(data.to_string())

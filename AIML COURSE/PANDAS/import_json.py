# importing json file 

import pandas as pd
data=pd.read_json("data.json")
# prints some data 
print(data)

print("....................................")
# prints all data 
print(data.to_string())
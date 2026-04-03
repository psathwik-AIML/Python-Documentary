# it is a 2 dimensional like tabular

import pandas as pd

data={"name":["captain","thor","tony"],
      "age":[30,43,52]}

df=pd.DataFrame(data,["a","b","c"])

# adding new column 
df["power"]=["shield","hammer","suit"]
# adding new row 

# create a new frame 
new_row=pd.DataFrame([{"name":"hulk","age":31,"power":"gama"}],["d"])

print(pd.concat([df,new_row]))
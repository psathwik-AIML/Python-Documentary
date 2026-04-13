import pandas as pd

# data cleaning is the process of fixing or removing unnecesary incorrect data 

df=pd.read_json("data.json")

# drop irrelavent columns 
new_data=df.drop(columns=["logins_count","email","user_id","updated_at","created_at"])
print(new_data.to_string())

print("....................................")

# remove columns which have nan 
new_data=df.dropna(subset=["last_login"])
print(new_data.to_string())

print(".........................................")
# replace columns which have nan 
new_data=df.fillna({"last_login":"coder"})
print(new_data.to_string())
# fix inconsistent values  replace any thing 
print(".........................................") 
new_data["email_verified"]=new_data["email_verified"].astype(str).replace({"True":"yes"})
print(new_data.to_string())
# standardize text
print(".........................................") 
new_data["given_name"]=new_data["given_name"].str.upper()
print(new_data.to_string())
# changing data type
print(".........................................") 
new_data["email_verified"]=new_data["email_verified"].astype(bool)
print(new_data.to_string())

# remove duplicates
print(".........................................") 
dupes=pd.read_csv("duplicates.csv")
print("Before")
print(dupes.to_string()) 
dupes=dupes.drop_duplicates()
print("After")
print(dupes.to_string()) 


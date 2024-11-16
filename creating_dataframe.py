import pandas as pd
data={
    'name':["Aksh","Ruchi","Pranjal"],
    'age':[23,24,22],
    'city':["Pune","Manchar","Nagar"]}
df=pd.DataFrame(data)
print(df) 
age=df['age']
city=df['city']
print(age)
print(city)
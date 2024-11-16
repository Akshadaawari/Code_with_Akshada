import pandas as pd
info={
    'sub':["Python","Mathematics","android"],
    'marks':[28,29,22],
    'grade':['A','B','c']
}
filter=pd.DataFrame(info)
print(filter)
s=filter['sub']
m=filter['marks']
print(s)
print(m)
filter_data=filter[filter['marks']>22]
print("The given filter data for dataFrame",filter_data)


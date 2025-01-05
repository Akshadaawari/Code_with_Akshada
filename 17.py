#17.Write a Python function to merge two dictionaries.
def merge_dict(dict1,dict2):
     dict1.update(dict2)
     return dict1 
    
d1={1:"Akshada" ,2:"Sangita",3:"Vishwajeet"}
d2={11:"Shreya",12:"Tanvi",13:"Smita"}
print("Mergig of two dictionaries are :",merge_dict(d1,d2))
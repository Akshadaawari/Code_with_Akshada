
#list=(1,2,3,4)
def max_multiplication(list):
    if len(list)<2:
        print(list)
    list.sort()
    product=list[0]*list[1]
    product2=list[-1]*list[-2]
    if product > product2:
        print(list[0],list[1])
    else:
        print(list[-1],list[-2])
num=[1,-2,3,-4,6,-7]
result=max_multiplication(num)
print(num)
    

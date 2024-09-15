x=[1,2,3,4,-4,-99,2]
sorted_list=sorted(x)
num1=sorted_list[-1]
num2=sorted_list[-2]
neg1=sorted_list[0]
neg2=sorted_list[1]
product1=num1*num2
product2=neg1*neg2
if product1>product2:
    print("the  two number",num1,num2)
else:
    print("the two numbers are",neg1,neg2)
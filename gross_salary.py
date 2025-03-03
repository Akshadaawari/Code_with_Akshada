#Assume a suitable value for ramesh salary. 
#his  dearness allowance is 40% of basic salary and house rent allowance is 20% of basic salary .
#write a program to calculate his gross salary


salary=int(input("Enter the salary :"))
dearness_allowance=40/100* salary
rent_allowance=20/100 *salary
gross_salary=dearness_allowance + rent_allowance + salary
print("Ramesh gross salary is",gross_salary)
print("Ramesh dearness_allowance is",dearness_allowance)
print("Ramesh rent allowance is",rent_allowance)
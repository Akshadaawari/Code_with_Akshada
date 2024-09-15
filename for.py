my_list=['akshada','rajaram','awari']
print(my_list)
for i in my_list:
    print(i)
print(my_list)
if 'rajaram' in my_list:
    print("yes,good name is present")

my_list[1]="father"
print(my_list)
my_list.append('patil')
print(my_list)

my_list[1:2]=["berry","strawberry","lichi","custurdapple"]
print(my_list)
#extend method
tuple=[1,2,3,4,5,6]
re=my_list.extend(tuple)
print(re)
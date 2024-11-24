a=[[2,3,4],[1,4,5,64],[3,6,9,12]]
sort_list=lambda x :(sorted(i) for i in x)
second_list=lambda x,f:[y[len(y)-2] for y in f(x)]
res=second_list(a,sort_list)
print(res)
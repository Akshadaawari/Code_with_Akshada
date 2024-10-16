row=int(input("Enter the total number of row  :"))
print("Total number of row",row)
for i in range(row):
    print(" "*(row-i),end=" ")
    print(" ".join(str(12**i)))
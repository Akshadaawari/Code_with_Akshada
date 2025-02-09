def sum_even_numbers(n):
    even_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even_sum += i
    return even_sum
num = int(input("Enter a positive integer: "))
print("sum",sum_even_numbers(num))
#39.Write a Python program to calculate the power of a number using recursion.
def power(base, exponent):
    # Base case: if the exponent is 0, return 1 (any number raised to the power of 0 is 1)
    if exponent == 0:
        return 1
    # Recursive case: base * power of the base raised to (exponent-1)
    else:
        return base * power(base, exponent - 1)

# Example usage
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")


#48.Write a Python program to find all prime numbers within a range.
def is_prime(num):
   
    if num < 2:
        return False
    

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
   
    primes = []
    
    
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    
    return primes


start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))


prime_numbers = find_primes_in_range(start, end)
print(f"Prime numbers in the range {start} to {end}: {prime_numbers}")

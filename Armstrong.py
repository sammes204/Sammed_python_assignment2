def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** power
    
    return total == n


# Example
num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

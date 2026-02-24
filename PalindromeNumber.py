def is_palindrome(n):
    original = n
    reverse = 0
    
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
        
    return original == reverse


num = int(input("Enter number: "))
print("Palindrome" if is_palindrome(num) else "Not Palindrome")

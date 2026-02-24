def reverse_number(n):
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n //= 10
    return reverse

print(reverse_number(1234))

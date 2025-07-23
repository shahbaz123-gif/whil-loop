base = 2
exponent = 8
result = 1
count = 0

while count < exponent:
    result *= base
    count += 1

print(f"{base}^{exponent} = {result}")
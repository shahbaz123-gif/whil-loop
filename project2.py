number = int(input("enter a number: "))
count = 0

#handle 0 as special case
if number == 0:
    count = 1
else:
    #convert to absolute value to handle negative numbers
    temp = abs(number)
    while temp > 0:
        temp = temp // 10 #remove last digit
        count += 1

print(f"total digits in {number}: {count}")            
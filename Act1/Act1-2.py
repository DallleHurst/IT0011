a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a > b) and (a > c):
    largest = a
elif (b > a) and (b > c):
    largest = b
else:
    largest = c

print("The largest number is:", largest)

if a >= b and a >= c:
    if b >= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a >= b:
        print(c, a, b)
    else:
        print(c, b, a)
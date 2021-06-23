# OddNumber.py
# Code to find the greatest odd number 

print('Enter 3 numbers')
x = int(input('Enter first number'))
y = int(input('Enter second number'))
z = int(input('Enter third number'))


if x%2 != 0:
    if y%2 != 0:
        if z%2 != 0:
            if x > y and x > z:
                print(x)
            elif y > x and y > z:
                print(y)
            else:
                print(z)
        elif x > y:
            print(x)
        else:
            print(y)
    elif z%2 != 0:
        if z > x:
            print(z)
        else:
            print(x)
    else:
        print(x)
elif y%2 != 0:
    if z%2 != 0:
        if y > z:
            print(y)
        else:
            print(z)
    else:
        print(y)
elif z%2 != 0:
    print(z)
else:
    print('No odd')
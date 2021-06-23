# piApproximation.py
#---------------------------------------------------------------------------------------------------
#   author: José Maia da Silva Neto
#   e-mail : maianeto2014@gmail.com
#---------------------------------------------------------------------------------------------------
#   This program calculates the approximation of pi with a specified precision
#   The user is asked for the number of terms to be used, which increases the precision


import math

x, y = 0, 0

n = eval(input("Enter the calculation precision based on the number of terms : "))

if ((n%2) != 0):
    ip = (n//2) + 1
    im = n//2
    c, d = 3, 1

    for i in range(ip):
        numberp = 4 / d
        x = x + numberp
        d = d + 4
    sp = x

    for i in range(im):
        numberm = 4 / c
        y = y - numberm
        c = c + 4
    sm = y

    result = sm + sp
    print(result)


if ((n%2) == 0):
    ip = n//2
    im = n//2
    c, d = 3, 1

    for i in range(ip):
        numberp = 4 / d
        x = x + numberp
        d = d + 4
    sp = x

    for i in range(im):
        numberm = 4 / c
        y = y - numberm
        c = c + 4
    sm = y

    result = sm + sp
    print(result)

print(abs(math.pi - result))
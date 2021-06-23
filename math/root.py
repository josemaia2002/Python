# root.py
#---------------------------------------------------------------------------------------------------
#   author: José Maia da Silva Neto
#   e-mail : maianeto2014@gmail.com
#---------------------------------------------------------------------------------------------------
#   This program calculates the approximation of a square root using the Newton's method
#   The user is asked for the radicand and the number of iterations to be used, which increases the precision


import math

x = eval(input("Enter a number: "))
n = eval(input("Number of iterations: "))
guess = x / 2

for i in range(n-1):
    guess = (guess + (x/guess)) / 2
    
print("Square root:", math.sqrt(x))
print("Number calculated", guess)
print("Precision: ", abs((math.sqrt(x)) - guess))

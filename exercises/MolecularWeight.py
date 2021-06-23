import math

print("Hydrocarbon molecular weight calculator")
h, c, o = eval(input("Enter the number of Hydrogen, Carbon and Oxygen atoms: "))
print("Hydrogen: ", h)
print("Carbon: ", c)
print("Oxygen: ", o)
print()
print()
mw = (1.0079 * h) + (12.011 * c) + (15.9994 * o)
print("Molecular weight: ", mw)
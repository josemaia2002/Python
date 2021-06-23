import math

print("Area calculator")
a, b, c = eval(input("Enter the lenght of the sides: "))
s = (a + b + c) / 2
area = math.sqrt((s * (s-a) * (s-b) * (s-c)))
print("The area of the triangle is: ", area)
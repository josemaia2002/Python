import math

radius = eval(input("Enter the radius: "))

volume = (4 / 3) * (math.pi * radius ** 3)
area = 4 * math.pi * radius **2

print("The volume is ", volume)
print("The surface area is ", area)
import math

price = eval(input("Enter the pizza price: "))
diameter = eval(input("Enter the pizza diameter: "))
area = math.pi * ((diameter / 2) ** 2)

AreaCost = price / area
print("Pizza area: ", area)

print("The cost per square centimeter is ", AreaCost, "reais per square cm")
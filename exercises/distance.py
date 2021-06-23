import math

x1, y1, x2, y2 = eval(input("Enter the coordinates of two points: "))
distance = math.sqrt((((x2-x1) ** 2) + ((y2-y1) ** 2)))
print("The distance between the points (", x1, ",", y1, ") and (" , x2, ",", y2, ") is", distance)

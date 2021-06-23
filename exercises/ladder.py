import math

print("Ladder lenght calculator")
height = eval(input("Enter the wall height: "))
angle = math.radians(eval(input("Enter the angle of the ladder: ")))
lenght = height / (math.sin(angle))
print(lenght)
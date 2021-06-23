print("Sum of a natural numbers series")
n = eval(input("Enter the number of elements: "))
x = 0

for i in range(n):
    number = eval(input("Enter a number: "))
    x = x + number
print(x)
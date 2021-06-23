print("Sum of the cubes of the first n natural numbers")
n = eval(input("Enter the number of elements: "))
x = 0

for i in range(1, n+1):
    i = i ** 3
    x = x + i
print(x)
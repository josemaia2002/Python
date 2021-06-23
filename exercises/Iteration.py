numbers = []
oddnumbers = []

for i in range(3):
    numbers.append(int(input('Enter a number: ')))

for j in range(3):
    if numbers[j] % 2 != 0:
        oddnumbers.append(numbers[j])

if len(oddnumbers) > 0:
    x = len(oddnumbers)
    oddnumbers.sort()
    print(oddnumbers[x - 1])
else:
    print('No odd')
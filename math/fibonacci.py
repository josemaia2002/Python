# fibonacci.py
#---------------------------------------------------------------------------------------------------
#   author: José Maia da Silva Neto
#   e-mail : maianeto2014@gmail.com
#---------------------------------------------------------------------------------------------------
#   This program calculates a fibonacci sequence element 
#   The user is asked for the element index, and the program calculates the element



sequence =  []

n = eval(input("Enter the element index: "))

sequence.insert(0, 1)
sequence.insert(1, 1)

for i in range(2, n):
    sequence.insert(i, (sequence[i-1] + sequence[i-2]))

print(sequence[n-1])
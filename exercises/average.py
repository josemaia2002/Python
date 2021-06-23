# average.py
#   A program to average two numbers

def main():                                                             #Defines the function main()
    print("Average calculator")                                         #Program introduction
    num1 = eval(input("Enter the first number "))                       #Asks the user to insert the first number and it's assigned to the variable 'num1'
    num2 = eval(input("Enter the second number "))                      #Asks the user to insert the second number and it's assigned to the variable 'num2'
    avg = (num1 + num2) / 2                                             #Calculates the average between 'num1' and 'num2' and assigned the result to the variable 'avg'
    print("The average between", num1, "and", num2, "is", avg)          #Prints the average between 'num1' and 'num2'
main()                                                                  #Calls the function main()
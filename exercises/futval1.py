# futval1.py
#   A program that calculates the future value of an investment
#   It requires the principal, annual percentage rate and investment time

def main():                                                             #Defines the function main()
    print("Future value calculator ")                                   #Program introduction
    principal = eval(input("How much do you want to invest? "))         #Asks the user to insert the principal
    apr = (eval(input("What is the annual interest rate? " ))) / 100    #Asks the user to insert the annual percntage rate
    time = eval(input("For how many years? "))                          #Asks the user to insert the investment time
    for i in range (time):                                              #Defines a counted for loop 
        principal = principal * (1 + apr)                               #Calculates the compound interest
    print("The value in", time, "years will be", end=" ")               #Prints the future value
    print(principal, "dollars")
main()                                                                  #Calls the function main()
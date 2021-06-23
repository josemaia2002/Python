# futval2.py
#   A program that calculates the future value of an investment
#   It requires the financial injection per year, annual percentage rate and investment time in years

def main():                                                             #Defines the function main()
    print("Future value calculator ")                                   #Program introduction
    injection = eval(input("Enter the annual money injection"))         #Asks the user to insert the money injection
    apr = (eval(input("What is the annual interest rate? " ))) / 100    #Asks the user to insert the annual percentage rate
    time = eval(input("For how many years? "))                          #Asks the user to insert the investment time
    principal = injection * (1 + apr)                                   #Calculates the coumpound interest for 1 year
    if(time > 1):                                                       #Verify if the investment time is greater than 1 year
        for i in range (time - 1):                                      #Defines a counted for loop 
            principal = (principal + injection) * (1 + apr)             #Calculates the compound interest
    print("The value in", time, "years will be", end=" ")               #Prints the future value
    print(principal, "dollars")
main()                                                                  #Calls the function main()
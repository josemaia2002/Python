# TemperatureConverter.py
#   A program to convert the temperature from Celsius to Farenheit

def main():                                                                 #Defines the function main()
    print("Temperature converter")                                          #Program introduction
    celsius = float(input("Enter the temperature in Celsius."))             #Asks the user to insert the temperature and it's assigned to the variable 'celsius'
    farenheit = (celsius * (9/5)) + 32                                      #Converts the temperature from Celsius to Farenheit
    print("The temperature in Farenheit is ", farenheit, " degrees.")       #Prints the temperature in Farenheit
main()                                                                      #Calls the function main()
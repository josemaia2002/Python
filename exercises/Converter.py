# converter.py
#   A program to convert units 

def ConvertFarenheit():                                                     #Defines the function ConvertFarenheit()
    print("Temperature converter")                                          #Program introduction
    print("Convert from Celsius to Farenheit")                                      
    celsius = float(input("Enter the temperature in Celsius."))             #Asks the user to insert the temperature and it's assigned to the variable 'celsius'
    farenheit = (celsius * (9/5)) + 32                                      #Converts the temperature from Celsius to Farenheit
    print("The temperature in Farenheit is ", farenheit, " degrees.")       #Prints the temperature in Farenheit
  

def ConvertCelsius():                                                       #Defines the function ConvertCelsius()    
    print("Temperature converter")                                          #Program introduction
    print("Convert from Farenheit to Celsius")
    farenheit = float(input("Enter the temperature in Farenheit."))         #Asks the user to insert the temperature and it's assigned to the variable 'farenheit'
    celsius = (farenheit - 32) * (5 / 9)                                    #Converts the temperature from Farenheit to Celsius  
    print("The temperature in Celsius is ", celsius, " degrees.")           #Prints the temperature in Celsius


def ConvertTemperature():
        choice = str(input("Choose between Farenheit and Celsius "))
        if(choice == 'farenheit'):
            ConvertFarenheit()
        elif(choice == 'celsius'):
            ConvertCelsius()
        else:
            print("No unit selected")
                                                                                

def ConvertMile():                                                          #Defines the function ConvertMile()
    print("Distance converter")                                             #Program introduction
    print("Convert from Kilometers to Miles") 
    km = float(input("Enter the distance in km "))                          #Asks the user to insert the distance and it's assigned to the variable 'km'
    miles = km * 0.62                                                       #Converts the distance from Kilometers to Miles  
    print("The distance in Miles is ", miles)                               #Prints the distance in Miles


def ConvertKm():                                                            #Defines the function ConvertKm()
    print("Distance converter")                                             #Program introduction
    print("Convert from Miles to Kilometers") 
    miles = float(input("Enter the distance in mi "))                       #Asks the user to insert the distance and it's assigned to the variable 'miles'
    km = miles / 0.62                                                       #Converts the distance from Miles to Kilometers   
    print("The distance in Kilometers is ", km)                             #Prints the distance in Kilometers


def ConvertDistance():                                                      #Defines the function ConvertDistance()
        choice = str(input("Choose between Kilometers and Miles "))
        if(choice == 'kilometers'):
            ConvertKm()
        elif(choice == 'miles'):
            ConvertMile()
        else:
            print("No unit selected")


unit = str(input("Choose between temperature and distance "))

if(unit == 'distance'):
    ConvertDistance()
elif(unit == 'temperature'):
    ConvertTemperature()
else:
    print("No quantity selected")
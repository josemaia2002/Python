# DistanceConverter.py
#   A program to convert the distance from Kilometers to Miles  

def main():                                                                 #Defines the function main()
    print("Distance converter")                                             #Program introduction
    km = float(input("Enter the distance in km "))                          #Asks the user to insert the distance and it's assigned to the variable 'km'
    miles = km * 0.62                                                       #Converts the distance from Kilometers to Miles  
    print("The distance in Miles is ", miles)                               #Prints the distance in Miles
main()                                                                      #Calls the function main()
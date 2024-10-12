#!/usr/bin/env python3
# Jeff Bohn
# 10/10/2024
# Chapter 14
# main.py


##############################################
###############  Exercise 14-3 ###############
##############################################


from temperature import Temp

def display_menu():
    print("The Convert Temperatures program\n")
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenhit")
    print()

def convert_temp():
    option = int(input("Enter a menu option: "))
    if option == 1:
        fahrenheit = int(input("Enter degrees Fahrenheit: "))
        celcius_obj = Temp(fahrenheit, 0)
        print(f"Degrees Celsius: {round(celcius_obj.toCelcius, 2)}")
    elif option == 2:
        celcius = int(input("Enter degrees Celsius: "))
        fahrenheit_obj = Temp(0, celcius)
        print(f"Degrees Fahrenheit: {round(fahrenheit_obj.toFahrenheit, 2)}")
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        
        again = input("Convert another temperature? (y/n): ")
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()



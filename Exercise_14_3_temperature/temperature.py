#!/usr/bin/env python3
# Jeff Bohn
# 10/12/2024
# Chapter 14
# temperature.py



class Temp:
    def __init__(self, fahrenheit, celcius):
        self.__fahrenheit = fahrenheit
        self.__celcius = celcius

    @property
    def toCelcius(self): 
        self.__celcius = (self.__fahrenheit - 32) * 5/9
        return self.__celcius
    
    @toCelcius.setter
    def toCelcius(self, new_value): 
        self.__celcius = new_value 
        self.__fahrenheit = (self.__celcius * 9 / 5) + 32     # update fahrnheit too 
        
    @property
    def toFahrenheit(self):
        self.__fahrenheit = (self.__celcius * 9 / 5 ) + 32
        return self.__fahrenheit

    @toFahrenheit.setter
    def toFahrenheit(self, new_value): 
        self.__fahrenheit = new_value
        self.__celcius = (self.__fahrenheit - 32) * 5 / 9     # update celcius too

























# class Temp:
#     def __init__(self, fahrenheit, celsius):
#         self.__fahrenheit = fahrenheit
#         self.__celsius = celsius

#     def to_celsius(self):
#         self.__celsius = (self.__fahrenheit - 32) * 5/9
#         return self.__celsius

#     def to_fahrenheit(self):
#         self.__fahrenheit = self.__celsius * 9 / 5 + 32
#         return self.__fahrenheit














# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit equals", round(to_celsius(temp), 2), "Celsius")
    
    for temp in range(0, 100, 20):
        print(temp, "Celsius equals", round(to_fahrenheit(temp), 2), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()


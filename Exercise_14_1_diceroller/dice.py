#!/usr/bin/env python3
# # Jeff Bohn
# 10/6/2024
# Chapter 14
# dice.py 

import random
from dataclasses import dataclass
from dice_images import dice_image_string

@dataclass
class Die:
    __value:int = 1

    # def __post__init__ (self):
    #     self.__value = self.roll()
    #     print(self.__value)

    @property
    def value(self):
        return self.__value
 
    @property
    def image(self):
        return dice_image_string()
                   
    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value can't be less than 1 or more than 6")
        else:
            self.__value = value
                
    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value
                
class Dice:
    
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        return tuple(self.__list)
                
    def rollAll(self):
        for die in self.__list:
            die.roll()

    def get_total(self):
        total = 0  
        for die in self.__list:
            total += die.value  
        return total











# import random
# from dataclasses import dataclass

# @dataclass
# class Die:
#     __value:int = 1

#     @property
#     def value(self):
#         return self.__value
                
#     @value.setter
#     def value(self, value):
#         if value < 1:
#             raise ValueError("Die value can't be less than 1.")
#         else:
#             self.__value = value
                
#     def roll(self):
#         self.__value = random.randrange(1, 7)

                
# class Dice:
    
#     def __init__(self):
#         self.__list = []

#     def addDie(self, die):
#         self.__list.append(die)

#     @property
#     def list(self):
#         return tuple(self.__list)
                
#     def rollAll(self):
#         for die in self.__list:
#             die.roll()

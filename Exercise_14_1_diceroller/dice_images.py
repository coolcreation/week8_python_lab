#!/usr/bin/env python3
# # Jeff Bohn
# 10/6/2024
# Chapter 14
# dice_images.py


def dice_image_string():
    
    one = " _____ \n" + \
          "|     |\n" + \
          "|  o  |\n" + \
          "|_____|"

    two = " _____ \n" + \
          "|o    |\n" + \
          "|     |\n" + \
          "|____o|"

    three = " _____ \n" + \
           "|o    |\n" + \
           "|  o  |\n" + \
           "|____o|"

    four = " _____ \n" + \
           "|o   o|\n" + \
           "|     |\n" + \
           "|o___o|"

    five = " _____ \n" + \
           "|o   o|\n" + \
           "|  o  |\n" + \
           "|o___o|"

    six = " _____ \n" + \
          "|o   o|\n" + \
          "|o   o|\n" + \
          "|o___o|"

    dice_list = [one, two, three, four, five, six]
        
    return dice_list

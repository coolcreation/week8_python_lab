#!/usr/bin/env python3
# Jeff Bohn
# 10/6/2024
# Chapter 14
# main.py


##############################################
###############  Exercise 14-1 ###############
##############################################


from dice import Dice, Die

def main():
    print("\nThe Dice Roller program")

    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    choice = "y"
    while choice.lower() == "y":        
        dice.rollAll()

        print("YOUR ROLL: ", end="")
        for die in dice.list:
            print(die.value, end = " ")
            
        print()
        #total = 0
        for die in dice.list:
            for i, img_die in enumerate(die.image):
                if i == int(die.value - 1):
                  #total = total + die.value
                  print(img_die)
                 
        print(f"\nTOTAL: {dice.get_total()}")
        #print(total)
        
        choice = input("Roll again? (y/n): ")
        
    print("Bye!")

if __name__ == "__main__":
    main()

"""
#! python3
Because, our mother try hard to think and figure out which food need to prepare
"""
import random
__author__ = 'rahuladream'
carbs = ["Oatmeal", 
            "Yams", 
            "Brown rice",
            "Sweet potatoes",
            "White potatoes with skin", 
            "wheat bread", 
            "Beans",
            "Pumpkin"]
protien = ["Eggs", 
            "Fish", 
            "Soy",
            "White-meat",
            "Pulses",
            "Nuts",]
veggies = ["baingan",
            "chukandar",
            "karela",
            "patta gobhi",
            "phool gobhi",
            "bhindi",
            "kaddu"]

for i in range(11):
    print("Option "+ str(i+1) + " will be " \
            + carbs[random.randint(0, len(carbs) -1)] \
            + " with " \
            + veggies[random.randint(0, len(veggies) - 1)] \
            + " and " \
            + protien[random.randint(0, len(protien) -1)]
            )

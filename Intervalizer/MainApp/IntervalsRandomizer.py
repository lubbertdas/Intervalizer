'''
Created on 14 Jul 2021

@author: ranka
'''

import random

def Randomizer():

    interval_output = ""
    fret = (0,1,2,3,4)
    string = (3,4,5,6)
    
    for i in range(6):
        interval_output = interval_output + "string: " + str(string[random.randint(0,len(string)-1)])
        interval_output = interval_output + ", fret: " + str(fret[random.randint(0,len(fret)-1)]) + "\n"
        
    return interval_output

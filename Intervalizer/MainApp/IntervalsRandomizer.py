import random

def Randomizer():

    interval_output = ""
    scale_range = []
        
    for guitar_string in reversed(range(1,7)):
        for fret in range(5):
            scale_range.append({"guitar_string": guitar_string, "fret":fret})
        
    for i in range(6):
        note = random.randint(3,17)
        interval_output = interval_output + "string: " + str(scale_range[note]["guitar_string"]) + ", fret: " + str(scale_range[note]["fret"]) + "\n"
        
    return interval_output


print(Randomizer())

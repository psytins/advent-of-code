# Link to Day 06 - https://adventofcode.com/2022/day/6
import sys
input = sys.argv[1] # get the input file

## PART ONE -----------
def part01():
    SOPmarker = list()
    repeat = False
    SOPindicator = 3
    SOPcounter = 0
    SOProutine = 0
    
    for x in open(input).read():
        if SOPcounter != SOPindicator: #get the 3 most recent
            SOPmarker.append(x) 
        else: # analyze 
            repeat = False

            SOPmarker.append(x) #add the 4th here
            if len(set(SOPmarker)) != len(SOPmarker):
                SOPmarker.pop(0)
                SOPcounter = 2
                repeat = True

            if not repeat:
                SOProutine += 1
                break

        SOPcounter += 1
        SOProutine += 1

    #Display
    print(f"{SOProutine} routines")
    print(f"marker: {SOPmarker}")


## PART TWO -----------
def part02():
    SOPmarker = list()
    repeat = False
    SOPindicator = 13 #change here the distinct chars (distinct_characters - 1)
    SOPcounter = 0
    SOProutine = 0
    
    for x in open(input).read():
        if SOPcounter != SOPindicator: #get the 3 most recent
            SOPmarker.append(x) 
        else: # analyze 
            repeat = False

            SOPmarker.append(x) #add the 4th here
            if len(set(SOPmarker)) != len(SOPmarker):
                SOPmarker.pop(0)
                SOPcounter = 12 #change here the distinct chars (distinct_characters - 2)
                repeat = True

            if not repeat:
                SOProutine += 1
                break

        SOPcounter += 1
        SOProutine += 1

    #Display
    print(f"{SOProutine} routines")
    print(f"marker: {SOPmarker}")


## Auxiliary ---------------
# Link to Day 03 - https://adventofcode.com/2022/day/3
import sys
input = sys.argv[1] # get the input file

## PART ONE -----------
def part01():
    priority_sum = 0
    priority = 0
    for x in open(input).read().split("\n"):
        half_index = int(len(x) / 2)

        first_slot = x[0:half_index]
        second_slot = x[half_index:]

        repeated_char = compare_strings(first_slot,second_slot)

        if repeated_char.isupper():
            priority = ord(repeated_char) - 38 # ascii
        elif repeated_char.islower():
            priority = ord(repeated_char) - 96 # ascii
        
        priority_sum += priority
        
        #print(f"{repeated_char} ( {priority} ) in {first_slot} / {second_slot}")

    print(priority_sum)

#Lowercase item types a through z have priorities 1 through 26.         97 to 122 in ascii ( -96 to get the right priority)
#Uppercase item types A through Z have priorities 27 through 52.        65 to 90 in ascii ( -38 to get the right priority)

## PART TWO -----------
def part02():
    priority_sum = 0
    priority = 0
    counter = 0
    for x in open(input).read().split("\n"):
        if counter == 0:
            first_bag = x
        elif counter == 1:
            second_bag = x
        elif counter == 2:
            third_bag = x

            repeated_char = compare_strings(first_bag,second_bag,third_bag)

            if repeated_char.isupper():
                priority = ord(repeated_char) - 38 # ascii
            elif repeated_char.islower():
                priority = ord(repeated_char) - 96 # ascii
            
            priority_sum += priority
            
            #print(f"{repeated_char} ( {priority} ) in {first_bag} / {second_bag} / {third_bag}")

            counter = -1
        counter += 1

    print(priority_sum)

## Auxiliary ---------------
def compare_strings(str1, str2): #compare two string char by char and return repeated char
    for c1 in str1:
        for c2 in str2:
            if(c1 == c2):
                return c1
    return -1

def compare_strings(str1, str2, str3): #compare three string char by char and return repeated char
    for c1 in str1:
        for c2 in str2:
            for c3 in str3:
                if(c1 == c2 == c3):
                    return c1
    return -1
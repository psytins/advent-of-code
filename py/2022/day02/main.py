# Link to Day 02 - https://adventofcode.com/2022/day/2
import sys
input = sys.argv[1] # get the input file

## PART ONE -----------
def part01():
    total_score = 0
    for x in open(input).read().split("\n"):  
        if(x[0] == 'A'): #Rock
            if(x[2] == 'X'): #Rock
                total_score += 1 + 3
            if(x[2] == 'Y'): #Paper
                total_score += 2 + 6
            if(x[2] == 'Z'): #Scissor
                total_score += 3 + 0

        elif(x[0] == 'B'): #Paper
            if(x[2] == 'X'):
                total_score += 1 + 0
            if(x[2] == 'Y'):
                total_score += 2 + 3
            if(x[2] == 'Z'):
                total_score += 3 + 6

        elif(x[0] == 'C'): #Scissor
            if(x[2] == 'X'):
                total_score += 1 + 6
            if(x[2] == 'Y'):
                total_score += 2 + 0
            if(x[2] == 'Z'):
                total_score += 3 + 3

    print(total_score)

## PART TWO -----------
def part02():
    total_score = 0
    for x in open(input).read().split("\n"):  
        if(x[0] == 'A'): #Rock
            if(x[2] == 'X'): #lose
                total_score += 3 + 0
            if(x[2] == 'Y'): #draw
                total_score += 1 + 3
            if(x[2] == 'Z'): #win
                total_score += 2 + 6

        elif(x[0] == 'B'): #Paper
            if(x[2] == 'X'):
                total_score += 1 + 0
            if(x[2] == 'Y'):
                total_score += 2 + 3
            if(x[2] == 'Z'):
                total_score += 3 + 6

        elif(x[0] == 'C'): #Scissor
            if(x[2] == 'X'):
                total_score += 2 + 0
            if(x[2] == 'Y'):
                total_score += 3 + 3
            if(x[2] == 'Z'):
                total_score += 1 + 6

    print(total_score)

part02()
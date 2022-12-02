# Link to Day 01 - https://adventofcode.com/2022/day/1
import sys

input = sys.argv[1] # get the input file

sum_of_calories = 0
higher_sum_of_calories = 0

for x in open(input).read().split("\n"):
    if x.strip():
        n = int(x)
        sum_of_calories = sum_of_calories + n

    if x == "":
        if sum_of_calories > higher_sum_of_calories:
            higher_sum_of_calories = sum_of_calories
        
        sum_of_calories = 0
            
print(higher_sum_of_calories)
# Link to Day 04 - https://adventofcode.com/2022/day/4
import sys
input = sys.argv[1] # get the input file

## PART ONE -----------
def part01():
    ans = 0
    for x in open(input).read().split("\n"):
        first_elf = x.split(",")[0].split("-")
        second_elf = x.split(",")[1].split("-")

        if check_fully_contains(int(first_elf[0]), int(first_elf[1]), int(second_elf[0]), int(second_elf[1])):
            ans += 1

    print(ans)

## PART TWO -----------
def part02():
    ans = 0
    for x in open(input).read().split("\n"):
        first_elf = x.split(",")[0].split("-")
        second_elf = x.split(",")[1].split("-")

        if check_fully_contains(int(first_elf[0]), int(first_elf[1]), int(second_elf[0]), int(second_elf[1])):
            ans += 1
        elif check_overlap(int(first_elf[0]), int(first_elf[1]), int(second_elf[0]), int(second_elf[1])):
            ans += 1
        
    print(ans)

## Auxiliary ---------------
def check_fully_contains(first_start, first_end, second_start, second_end):
    return ((first_start - second_start) <= 0) and ((first_end - second_end) >= 0) or ((first_start - second_start ) >= 0) and ((first_end - second_end) <= 0)

def check_overlap(first_start, first_end, second_start, second_end):
    for x in range(first_start, first_end + 1):
        for y in range(second_start, second_end + 1):
            if x == y:
                return True
    return False
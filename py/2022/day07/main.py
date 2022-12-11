# Link to Day 07 - https://adventofcode.com/2022/day/7 (INCOMPLETE)
import sys
input = sys.argv[1] # get the input file

## PART ONE -----------
def part01():
    folder_size = dict()
    nested_folder = dict()
    current_folder = "/"
    INPUT_SYMBOL = '$'
    CD = 'cd'
    LS = 'ls'
    DIR = 'dir'

    for x in open(input).read().split("\n"):
        command = x.split()
        if command[0] == INPUT_SYMBOL:
            if command[1] == CD:
                current_folder = command[2]
            elif command[1] == LS:
                pass
        elif command[0] == DIR:
            if current_folder in nested_folder:
                temp : list = nested_folder.get(current_folder) 
                temp.append(command[1])     
                nested_folder.update({current_folder:temp})
            else:
                nested_folder.update({current_folder:[command[1]]})

        elif command[0] != DIR:
            if current_folder in folder_size:
                add_size = folder_size.get(current_folder) + int(command[0])            
                folder_size.update({current_folder:add_size})
            else:
                folder_size.update({current_folder:int(command[0])})


    #print(folder_size)
    #print(nested_folder)

    #print(final)
    for r in nested_folder:
        if(folder_size.get(r) is not None):
            sum_of_dir = folder_size.get(r)
        for l in nested_folder.get(r):
            if(folder_size.get(l) is not None):
                sum_of_dir += folder_size.get(l)

        print(f"dir {r} ({sum_of_dir}):")
        for l in nested_folder.get(r):
            print(f"  - dir {l} ({folder_size.get(l)})")
        
        print()   

## PART TWO -----------
def part02():
    pass

## Auxiliary ---------------


part01()
# Link to Day 05 - https://adventofcode.com/2022/day/5
import sys
input = sys.argv[1] # get the input file

## PART ONE -----------
def part01():
    #Create a matrix of the boxes
    instructions = False
    box_line = list()
    box_total = list()
    for x in open(input).read().split("\n"):
        if instructions: #instructions zone. when reached here, box_total is full populated
            Move = int(x[5:7])
            From = int(x[12:14])
            To = int(x[17:])
            box_total = CrateMover9000(box_total,Move,From,To) #rearrange
        else:
            x = x.replace("    ", "[-]").replace(" ", "")
            for c in range(0,len(x)-1,3):
                box_line.append(x[c:c+3])
            box_total.append(box_line)
            box_line = []

        if x == "": # reach end of box sections
            box_total.pop()#remove garbage
            box_total.pop()#remove garbage
            instructions = True

    #Display
    for r in box_total:
        print(r)



## PART TWO -----------
def part02():
    #Create a matrix of the boxes
    instructions = False
    box_line = list()
    box_total = list()
    for x in open(input).read().split("\n"):
        if instructions: #instructions zone. when reached here, box_total is full populated
            Move = int(x[5:7])
            From = int(x[12:14])
            To = int(x[17:])
            box_total = CrateMover9001(box_total,Move,From,To) #rearrange
        else:
            x = x.replace("    ", "[-]").replace(" ", "")
            for c in range(0,len(x)-1,3):
                box_line.append(x[c:c+3])
            box_total.append(box_line)
            box_line = []

        if x == "": # reach end of box sections
            box_total.pop()#remove garbage
            box_total.pop()#remove garbage
            instructions = True

    #Display
    for r in box_total:
        print(r)


## Auxiliary ---------------

# CrateMover 9000--------
def CrateMover9000(stack_list:list, move:int, froM:int, to:int) -> list: 
    list_to_move = list()
    froM =  froM - 1
    to = to - 1
    EMPTY = "[-]"

    #pick the ones to move
    for cnt in range(len(stack_list)): #just to search for a empty space, run one time after it founds
        if stack_list[cnt][froM] != EMPTY:
            for mv in range(move): #layer
                list_to_move.append(stack_list[cnt+mv][froM])
                stack_list[cnt+mv][froM] = EMPTY
            break

    #put in the right stack
    move_count = 0
    for cnt in range(len(stack_list)): #just to search for a empty space, run one time after it founds
        if stack_list[cnt][to] != EMPTY:
            cnt -= 1
            for mv in range(move): #layer
                
                if cnt-mv < 0:
                    stack_list.reverse()
                    stack_list.append([EMPTY for i in range(len(stack_list[cnt]))])
                    stack_list.reverse()
                    mv = cnt

                stack_list[cnt-mv][to] = list_to_move[move_count]
                move_count += 1
            return stack_list

    #in case empty stack
    cnt = len(stack_list) - 1
    for mv in range(move): #layer
        if cnt-mv < 0:
            stack_list.reverse()
            stack_list.append([EMPTY,EMPTY,EMPTY])
            stack_list.reverse()
            mv = cnt
        stack_list[cnt-mv][to] = list_to_move[mv]
    
    return stack_list

# CrateMover 9001 ----------------
def CrateMover9001(stack_list:list, move:int, froM:int, to:int) -> list: 
    list_to_move = list()
    froM =  froM - 1
    to = to - 1
    EMPTY = "[-]"

    #pick the ones to move
    for cnt in range(len(stack_list)): #just to search for a empty space, run one time after it founds
        if stack_list[cnt][froM] != EMPTY:
            for mv in range(move): #layer
                list_to_move.append(stack_list[cnt+mv][froM])
                stack_list[cnt+mv][froM] = EMPTY
            break

    list_to_move.reverse()

    #put in the right stack
    move_count = 0
    for cnt in range(len(stack_list)): #just to search for a empty space, run one time after it founds
        if stack_list[cnt][to] != EMPTY:
            cnt -= 1
            for mv in range(move): #layer
                
                if cnt-mv < 0:
                    stack_list.reverse()
                    stack_list.append([EMPTY for i in range(len(stack_list[cnt]))])
                    stack_list.reverse()
                    mv = cnt

                stack_list[cnt-mv][to] = list_to_move[move_count]
                move_count += 1
            return stack_list

    #in case empty stack
    cnt = len(stack_list) - 1
    for mv in range(move): #layer
        if cnt-mv < 0:
            stack_list.reverse()
            stack_list.append([EMPTY,EMPTY,EMPTY])
            stack_list.reverse()
            mv = cnt
        stack_list[cnt-mv][to] = list_to_move[mv]
    
    return stack_list
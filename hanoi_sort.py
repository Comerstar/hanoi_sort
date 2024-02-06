
import random

# Comp must be a comparator function
def hanoi_sort(comp, lst):
    stacks = [lst, [], []]
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if x != y:
            if len(stacks[x]) == 0:
                if len(stacks[y]) == 0:
                    # Check if the final stack is sorted
                    z = 3 - x - y
                    sorted = True
                    for i in range(len(stacks[z]) - 1):
                        if comp(stacks[z][i], stacks[z][i+1]) <= 0:
                            sorted = False
                            break
                    if sorted:
                         return stacks[z]
            elif len(stacks[y]) != 0:
                # Check if action is valid and if so perform it
                if (comp(stacks[x][-1], stacks[y][-1]) <= 0):
                    stacks[y].append(stacks[x][-1])
                    stacks[x].pop()
            else:
                stacks[y].append(stacks[x][-1])
                stacks[x].pop()

test = []
print("Input the integers of your list, then a non-integer.")
user_in = input()
try:
    while True:
        test.append(int(user_in))
        print("Inputted ", test)
        user_in = input()

except Exception:
    print(test)
    print(hanoi_sort(lambda x, y: y - x, test))

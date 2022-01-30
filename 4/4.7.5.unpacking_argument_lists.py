# Official Documentation
# 4.7. More on defining functions
# Unpacking argument lists

# part 1
lis = list(range(3, 6))
print(lis)

args = [3, 6]
print(list(range(*args)))

# part 2
def parrot(voltage, state = 'a stiff', action = 'voom'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.", end = ' ')
    print("E's", state, "!")

d = {"voltage":"four million", "state":"bleedin ' demised", "action":"VOOM"}
parrot(**d)

# code worked as expected
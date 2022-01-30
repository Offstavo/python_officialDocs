# Official Documentation
# 4.7. More on defining functions
# Keyword arguments

# part 1
def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)  # 1 positional argument
parrot(voltage = 1000) # 1 keyword argument
parrot(voltage = 1000000, action = 'VOOOOOM') # 2 keyword arguments
parrot(action = 'VOOOOOM', voltage = 1000000) # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump') # 3 positions arguments
parrot('a thousand', state = 'pushing up the diasies') # 1 postional, 1 keyword

# part 2
# argument * receives a tuple
# argument ** receives a dictionary
# * must come before **
def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            shopkeeper = "Michael Palin",
            client = "John Cleese",
            sketch = "Cheese Shop Sketch")

# code worked as expected
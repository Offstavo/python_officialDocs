# Official Documentation
# 4.7. More on defining functions
# Function Annotations

# part 1
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotaions", f.__annotations__)
    print("Arguments", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

# code worked as expected
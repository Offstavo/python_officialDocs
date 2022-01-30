# Official Documentation
# 4.7. More on defining functions
# Lambda expressions

# part 1
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(0))
print(f(1))

# part 2
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
pairs
print(pairs)

# code worked as expected
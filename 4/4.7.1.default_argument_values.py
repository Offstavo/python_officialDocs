# Official Documentation
# 4.7. More on defining functions
# Default Argument Values

# part 1
def ask_ok(prompt, retries = 4, reminder = 'Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid response')
        print(reminder)

print(ask_ok('Do you really want to quit?'))
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# part 2
i = 5
def f(arg = i):
    print(arg)

i = 6
f()

# part 3
def f(a, l=[]):
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))

# part 4
def f(a, l = None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))

# code worked as expected
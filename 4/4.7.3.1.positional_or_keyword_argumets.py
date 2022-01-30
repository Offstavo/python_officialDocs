# Official Documentation
# 4.7. More on defining functions
# 4.7.3. Speicial Parameters
# Positional or keyword arguments

# positional or keyword, positional only and keyword only arguments
# use the following * or /


# part 1

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_examples(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)

standard_arg(arg = 2)

pos_only_arg(1)

kwd_only_arg(arg = 3)

combined_examples(1, 2, kwd_only =3)

combined_examples(1, standard = 2, kwd_only = 3)

# part 2
def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name':2})

# code worked as expected
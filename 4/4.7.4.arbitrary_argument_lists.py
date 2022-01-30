# Official Documentation
# 4.7. More on defining functions
# Arbitrary Argument Lists

# part 1
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# part 2
def concat(*args, sep = "/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus ", sep = "."))

# code worked as expected
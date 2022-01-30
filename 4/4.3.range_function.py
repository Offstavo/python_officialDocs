# 4.0 More Control Flow Tools
# range function

# part 1
for i in range(5):
    print(i)

# part 2
print(list(range(5,10)))

print(list(range(0,10,3)))

print(list(range(-10,-100,-30)))

# part 3
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range(10) is the same as range(0,10)
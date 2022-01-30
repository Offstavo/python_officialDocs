# 4.0 More Control Flow Tools
# For statements

# part 1
words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))

# part 2
users = {'Hans':'active', 'Elenore':'inactive', 'Yen':'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

# part 3
acitive_users = {}
for user, status in users.items():
    if status == 'acitve':
        active_users[user] = status

print(users)

# code worked as expected
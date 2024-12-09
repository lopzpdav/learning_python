## FOR STATEMENTS
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

# We can also use if inside the for
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(users)

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user] # we are deleting inactive users
        
# In the previous example, we need to iterate on the copy of "users"
# cause if we iterate while modifying the dictionary is not allowed
# and it'll result in RuntimeError

active_users = {} # we create a new dictionary only with active ones
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

## RANGE() FUNCTION
for i in range(5):
    print(i)

print(list(range(5, 10))) # arguments are start, stop
print(list(range(5, 10, 2))) # start, stop, step
print(list(range(-10, -100, -50))) # works with negative values too

text_list = ['Patricio', 'had', 'a', 'headache']
for i in range(len(text_list)): # we can iterate using lenght function
    print(i, text_list[i])
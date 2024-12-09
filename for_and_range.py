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

print(range(0,10)) # we can't print a range directly

# range isn't an actual list, it's a lazy object who generates numbers
# when needed, not store the numbers
# we can iterate over a range or use index o checking membership "in"

# the use of range is because of memory efficiency
range(1, 100000000) # this is lightweight in memory
list(range(1, 100000000)) # this consumes a lot of memory

# the term "lazy" means that the numbers are generated on-demand
# as you iterate, rather than pre-storing them

# On the other side, we can use range as argument for functions
print(sum(range(0, 4))) # 0 + 1 + 2 + 3
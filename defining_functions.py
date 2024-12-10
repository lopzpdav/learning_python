## CREATING FUNCTIONS
# at this point i can compare this with methods on java, clearly 
# java has explicit types, in python there isn't necessary to do that

def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n.""" # just documentation
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# we use the "def" keyword indicating that we are defining a function
# then we follow with the function name "fib" and the parenthesis for
# the formal parameters

fib # pointing the function
f = fib # pointing the spot on the memory where the "fib" function is
f(100) # and then assign the parameters, this should work

# the variable assignments in a function store the values in the local
# simbol table, but this table is created when the function is called,
# even we can point to the function and then pass the arguments like 
# above

# AND OBVIOUSLY A FUNCTION CANT RETURN A VALUE, like this case
# just printing, the default value returned is "None", normally suppressed
# by the interpreter
print(fib(0)) # just to know

# and this is an example returning a value for the same purpose

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result

## DEFAULT ARGUMENT VALUES
# is obvious how this works, it's just to know that we can use default
# argument values, like "retries" in this case and use it for the logic

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}: # "in" keyword is like sql
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok(input('Please enter the prompt'))
# ask_ok('yes', 1, 'nice try') 
# we can override the default arguments, the previous test are commented
# cause if we don't, the next ones will not work

i = 5 # we create the variable pointing to "5"

# the value has taken in the scope of definition
# it means that here the value "arg" on the function is "5"
def f(arg=i):
    print(arg)

i = 6 # this assignment should not be visible

f() # cause the function was pointing to the first value


# it's a bit different with objects like list, dictionaries, or instances
# in this case we are using "append" to add elements, and every time we 
# call the function the new value is saved, cause is pointing the same
# object

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# to avoid this behaviour, we can declare the argument like "None"
# basically cleaning the argument every time the function is called
def f_1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f_1(1))
print(f_1(2))
print(f_1(3))
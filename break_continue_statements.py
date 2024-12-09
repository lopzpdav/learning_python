## BREAK ENDS THE LOOP
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break # when we reach this line, the loop will end
        
## CONTINUE ENDS THE ACTUAL ITERATION AND CONTINUE WITH THE NEXT ONE
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

## ELSE CLAUSES ON LOOPS
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# By using else on loops we can do some action if the break line isn't reached
# in this case "else" belongs to the "for" loop, not for the "if" conditional

## PASS STATEMENTS
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# we can use for creating minimal classes
class MyEmptyClass:
    pass

# we can use as a place-holder for a function when we are working in
# new code
def initlog(*args):
    pass   # Remember to implement this!
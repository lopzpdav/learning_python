## MATCH STATEMENTS
# match is like a "switch" on java or c++

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 405:
            return "Conflict"
        case 401 | 403 | 404: # we can use "|" for "or"
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

# the “variable name” _ acts as a wildcard and never fails to match. 
# If no case matches, none of the branches is executed.
# I mean, is probably like "default" in a "switch" for java

print(http_error(400))
print(http_error(500)) # confirmed, is like "default" for java switch

point = (0, 1)
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is (point_instance):
    match point_instance:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))

class Point_Match_Args:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
# We can use __match_args__ built-in function to specify the names of
# the attributes that should be used when performing pattern matching
# with the positional patterns inside the "match" statement

points = [Point_Match_Args(0, 0)]

match points:
    case []:
        print("No points")
    case [Point_Match_Args(0, 0)]:
        print("The origin")
    case [Point_Match_Args(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point_Match_Args(0, y1), Point_Match_Args(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

# As we see in the examples above, we can make a case for non specific 
# values, and we can work with classes

point_two = Point_Match_Args(5, 5)

match point_two:
    case Point_Match_Args(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point_Match_Args(x, y):
        print(f"Not on the diagonal")

# we can add an "if" clause to a pattern, known as a "guard", if the 
# guard is false, the "match" statement goes on to try the next case
# block

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
        
# And last but not least, we can use it with enums too, i mean, is
# clearly like the "switch" statement on java lol
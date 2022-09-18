#Import
#Import math it will help us to use bulit in functions like sine cos sqrt etc... from the math module
import math
# help(math) #It will display all the bulit in functions present in the math module
print(math.sqrt(4))
print(math.sin(90))
print(math.floor(3.456))
print(math.cos(90))

#or you can simply call from math import sqrt but in this case only sqrt get to be functioning no otherr functions like sin cos etc functions
from math import sqrt
print(sqrt(4))
print(cos(4))

# if we use from math import * we can use  all the bulit in functions from math module
from math import*
print(sqrt(4))
print(cos(0))
print(sin(0))

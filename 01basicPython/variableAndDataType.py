   #------ my first line  in python programming

# print("Hello World"); 

# --------- variables in Python 
#  ------- Creating Variables


a = 5
b = "Susy"
# print(b);

# ------- Casting
x = str(3) # x will be '3' string value 
y = int(4) # y will be 4 intiger value
z = float(3) # z will be 3.0 this float value 

print(x);
print(y);
print(Z);

# ------- get the type using type 

print(type(x)) # ----- type is str
print(type(y)) # ----- type is int
print(type(z)) # ----- type is float

# -----------  Case-Sensitive
# ----------- This will create two variables:
a = 4
A = "Susy"
# ------------- A will not overwrite a
# print(a) # output 4
# print(A) # output susy


  # +++++++++++++++++++++ Python - Variable Names  +++++++++++++++++++++

# this  is ok 

#   myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# this  is not  ok 

# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Python Variables - Assign Multiple Values

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# One Value to Multiple Variables

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# print(x)
# print(y)
# print(z)

# -------- Output Variables

m = "python is awesome"
# print(m)

f = "python"
g = " is"
h = " awesome"
# print(f, g, h)
# print(f + g + h)

v = 5
t = 20
u = "susy"
# print( v + t)
# print(v + u) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(v , u)

# +++++++++++++ Python - Global Variables +++++++++++++++++

newVariable = "awesome!"

def myfunc():
  newVariable = "fantastic"
  print("python is " + newVariable)

myfunc()

print("python is " + newVariable )

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



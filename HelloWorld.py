# Printing Hello World
print("Hello World!")

# Printing sys.vversion
import sys

print(sys.version)

if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome2"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome3"
print(x + y + z)

x = 5
y = 10
print(x + y)
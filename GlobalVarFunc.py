x = "awesome"

def myfunc():
  
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



def myfunc2():
  global y
  y = "fantastic"

myfunc2()

print("Python is " + y)



global z
z = "fantasticccc"
def myfunc3():
    print("Python is " + z)

myfunc3()


a = "awesome"

def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)

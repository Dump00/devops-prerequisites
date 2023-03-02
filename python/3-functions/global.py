# c = 1

# def add():
#     c = c + 2
#     print(c)

# add()

# UnboundLocalError: local variable 'c' referenced before assignment
# This is because we can only access the global variable but cannot modify it from inside the function

c = 1

def add():
    global c
    c = c + 2
    print(c)


add()
print(c)




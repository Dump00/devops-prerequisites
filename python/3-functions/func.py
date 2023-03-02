import math

def greet():
    print('Hello!')
greet()


# return Type

def calc_sum(a, b):
    return a+b
sum = calc_sum(2, 3)
print(sum)


# Built in functions

sq_root = math.sqrt(4)
print(sq_root)

power = pow(2,3)
print(power)


# With Arbitrary Arguments

def total(*numbers):
    count = 0
    for i in numbers:
        count += i
    return count
total_count = total(1,2,3,4)
print(total_count)
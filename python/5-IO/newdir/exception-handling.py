# try:
#      code that may cause exception
# except:
#      code to run when exception occurs


try:
    num1 = int(input('num one:'))
    num2 = int(input('num two:'))
    result = num1 / num2
    print(result)
except:
    print("Error: Denominator cannot be 0")
finally:
    print('finally works!')




# Catching Specific Exceptions
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")
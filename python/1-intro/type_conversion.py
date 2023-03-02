# int() / str() / float()

int_number = 5
string_number = '7'

new_type1 = string_number + str(int_number)
print(new_type1, type(new_type1))

new_type2 = int_number + int(string_number)
print(new_type2, type(new_type2))


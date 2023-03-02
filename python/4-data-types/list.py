numbers = [1, 5, 2, 8]
print(numbers)

# append()
numbers.append(4)
print(numbers)


# extend()
num = [20, 35, 40]
numbers.extend(num)
print(numbers)


# change list items
numbers[0] = 6
print(numbers)


languages = ['Java', 'Python', 'Go', 'JS', 'c#']
print(languages[-1])
print(languages[2:4])


# len()
length = len(languages)
print(length)


# del()
del languages[-1]
print(languages)


# remove()
languages.remove('Python')
print(languages)


# Check if an Item Exists in the Python List
status = 'Java' in languages
print(status)


# index()
index = languages.index('Java')
print(index)
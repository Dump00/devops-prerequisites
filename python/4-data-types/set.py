# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}


# add()
empty_set.add(2)
empty_set.add(5)
print(empty_set)

another_empty_set = set()
another_empty_set.add(3)
another_empty_set.add(5)
print(another_empty_set)


# update()
empty_set.update(another_empty_set)
print(empty_set)
print(another_empty_set)


# discard()
another_empty_set.discard(5)
print(another_empty_set)


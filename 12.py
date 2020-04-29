# set cannot duplicate in set
s = {'banana', 'blueberry', 'rashberry'}
print(s)
s.add('strawberry')
s.add('banana')  # cannot at this element
print(s)


l = [1, 2, 3, 4, 3, 3, 4, 5, 6, 4]  # list
l = set(l)  # cast list to set
print(l)

library_1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
library_2 = {'Harry Potter', 'Romeo and Juliet'}
all_book_in_town = library_1.union(library_2)  # add 2 to 1
same_book = library_1.intersection(library_2)  # take the same of 2 library
# which library 1 have but do not exist in library 2
diff = library_1.difference(library_2)
print(all_book_in_town)
print(same_book)
print(diff)

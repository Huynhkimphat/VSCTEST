# Tuples
l = [1, 2, 3]  # list #can change the data
t = (1, 2, 3)  # tuple # cannot change the data
# print(t[0])

# every element in tuple can not change
# very sercure for you to store some of can not change data

person1 = ("Nancy-pants", 25, 'Pizza')
person2 = ("HKP", 19, 'Pasta')
people = [person1, person2]
# (name, age, favorfood) = person


for name, age, favorfood in people:
    print(name)
    print(age)
    print(favorfood)
    print()

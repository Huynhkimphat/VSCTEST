# List Comprehension

names = ['HKP', 'TKN', 'LTQ', 'LMT']
l = []

# for person in names:
#     l.append(person)
# print(l)

l = names
print(l)
# same
print([person for person in names])

a = [1, 2, 3, 4]
print([item*2 for item in a])

movie_and_rating = {"Intersteller": 9, "Dark Knight": 8, "50 Shades": 2, }
print([movie for movie in movie_and_rating if movie_and_rating[movie] > 6])

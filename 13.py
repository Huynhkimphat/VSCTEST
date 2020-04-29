from collections import OrderedDict
# dictionary

dic = {
    'Phat': 18,
    'Ngan': 18
}
# get== to get value but if this value does not exist,it will return none
print(dic.get('Phat'))
print(dic.get('Hello'))
# dic[''] to get value but if this value does not exist,it will error
print(dic['Phat'])  # same with the previous but
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())


contact = {
    'Joe': {'phone': 1234567, 'mail': 'hkimphat2012@gmail.com'},
    'Jane': {'phone': 151313, 'mail': 'hkimphat2013@gmail.com'}
}
# print(contact['Joe'])
print(contact)
contact.popitem()  # delete
print(contact)
contact.clear()
print(contact)


word_count = {
    'I': 1,
    'like': 3,
    'the': 2,
}
print(sorted(list(word_count.values())))

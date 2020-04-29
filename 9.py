# LISTS
# ADVANCED INDEXING && SLICING
# a = [1, 2, 4]
# print(a[2])
# names = ["A", "B", "C"]
# names.append("D")
# names.insert(2, "E")
# names.remove("B")
# names.reverse()
# print(names)
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[:3])
print(digits[-1:0:-2])
for i in range(len(digits)):
    print(digits[0:i])
window_size = 1
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])

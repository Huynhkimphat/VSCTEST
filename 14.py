# Mutability= Changeable(List,dic,order_dict)
# Immutability=Unchangeable(Tuple,int,float,booleans)

d = {'A': 1, 'B': 2, }  # the key are immutability

t = (1, 2, [1, 2, 3])
print(t)
t[2][0] = 7
print(t)

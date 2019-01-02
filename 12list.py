l = ['a', 'b', 'c', 'd', 'd', 'd']
l.append(1)
print(l)
# inseer elemnets in between
l.insert(0, 'x')
print(l)
# Removing Element with the index
l.pop(0)
print(l)
# Remocing Element by name-Removes the firsr index of the element
l.remove('a')
print(l)
del l[0:2]
print(l)
# Search Element with Index
x = l.index('f')
print(x)
# Getting Count
z = l.count('d')
print(z)

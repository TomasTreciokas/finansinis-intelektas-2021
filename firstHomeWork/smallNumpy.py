import numpy as np

# 1
a = np.random.randint(low=1, high=10, size=10)
b = np.random.randint(low=1, high=10, size=10)
c = a + b

print(np.sum(c))

# 2
a = np.random.randint(low=-10, high=10, size=10)

print('array values BEFORE modification: ' + str(a))

a[a > 0] = 0

print('array values AFTER modification: ' + str(a))

# 3
a = np.random.randint(low=1, high=10, size=10)
b = a[a > 6]

print('Before: ' + str(a))
print('After: ' + str(b))

# 4
a = np.random.randint(low=1, high=10, size=5)
values = np.unique(np.extract(a[1:] == a[:-1], a))
position = np.where(a[1:] == a[:-1])

print('Before: ' + str(a))
print('After: ' + str(values))
print('with position:' + str(position))

# 5
a = np.random.randn(10)
b = np.random.randn(1, 10)
rez = np.greater(a, b)
rez = np.where(rez == True)[1]
print('rezultatas: ' + str(type(rez)) + str(rez))

# 5 antra variacija
a = np.random.randint(low=1, high=10, size=20)
b = np.random.randint(low=1, high=10, size=20)
b = a[a > b]

# 6
a = np.random.randint(low=1, high=10, size=20)
b = np.append(a[1:],a[-1])

#7
a = np.random.randint(low=1, high=10, size=20)
b = np.flip(a)

#8

a = np.random.randint(low=1, high=10, size=20)
a[1::2] = 0

#9
a = np.random.randint(10, size=(2,4))
print(np.mean(a, axis=1))
print(np.mean(a, axis=0))

#10
a = np.random.randint(10, size=(4,4))
n = len(a)
d = a.ravel()[::n+1]
a = a[::-1]
g = a.ravel()[::n+1]
print(a)
print(d)
print(g)
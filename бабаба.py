#1.
'''
a = int(input())
b = int(input())
for i in range(a, b):
    if i % 7 == 0:
        print(i)
'''
#2.
'''
a = int(input())
b = int(input())
c = 0
for i in range(a, b):
    print(i)
    if i % 7 == 0:
        print(i)
for t in range(b, a):
    print(t)
    if i % 5 == 0:
        c += 1
        print(c)
'''
#3.
'''
a = int(input())
b = int(input())
c = "fizz"
d = "buzz"
for i in range(a, b):
    if i % 3 == 0:
        print(c)
    elif i % 5 == 0:
        print(d)
    elif i % 3 == 0 and i % 5 == 0:
        print(c, d)
    elif i % 3 != 0 and i % 5 != 0:
        print(i)
    else:
        print()
'''
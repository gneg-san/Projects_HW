import random
#1.
''' 
lelele = []
lelele2 = []
for i in range(10):
    lelele.append((random.randint(-10,10)))
for i in range(10):
    lelele2.append((random.randint(-10,10)))
lelele.sort()
lelele2.sort(reverse=True)

abudabi = lelele + lelele2

print(abudabi)
'''
#2.
lelele = []
lelele2 = []
lelele3 = []
for i in range(15):
    lelele.append((random.randint(-20,20)))
for i in range(15):
    lelele2.append((random.randint(-20,20)))
for i in range(15):
        lelele3.append((random.randint(-20, 20)))
abudabi = []
for i in lelele:
    if i // 2 == 0:
        abudabi.append(i)
amsterdam = []
for i in lelele2:
    lelele2.insert(0)
    lelele2.insert(len(lelele2))
    amsterdam.append(i)

print(amsterdam)

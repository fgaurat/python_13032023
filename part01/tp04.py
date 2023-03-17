from collections import deque

the_list = ['toto','tutu','titi']
the_list.append('une autre valeur')
print(the_list)
last = the_list.pop()
print("last",last)
print("the_list",the_list)

print(the_list.count("toto"))
print()
print(50*'-')

fifo = deque(["value"])

# fifo.insert(0, "first value")
fifo.appendleft("first value")
print(fifo)
print(type(fifo))
print(list(fifo))
# first_value = fifo.pop(0)
# print("first_value",first_value)
# print(fifo)

l = []
for i in range(10):
    l.append(i)

print(l)
l = list(map(lambda i:i,range(10)))
print(l)

l = [i for i in range(10)]
print(l)

print(50*'-')

t = 10,20,"toto"
a,b = 0,1
print(type(t))
print(t)


def f():
    return 0,1

a,b = f()
print(a)

print(50*'-')
s = {"toto","tutu","titi"}
print(s)
s.add("tata")
print(s)
for i in s:
    print(i)
print(50*'-')

d = {"login":"root","valid":True,"password":"12345"}

print(d)
print(d['login'])

for k in d:
    print(k,d[k])
print(list(d))
print(d.keys())
print(d.values())

l = ['valeur A','valeur B','valeur C']

for pos,value in enumerate(l):
    print(pos,value)

for key,value in d.items():
    print(key,value) 

header = ["login","valid","password"]
line = ["root",True,"12345"]

dict_csv = zip(header,line)
print(dict(dict_csv))
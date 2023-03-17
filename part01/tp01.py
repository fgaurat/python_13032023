import copy
# TheWorldIsFlat => UpperCamelCase 
# theWorldIsFlat => camelCase 
# the_world_is_flat => snake_case 
# the-world-is-flat => kebab-case 


the_world_is_flat = True
if the_world_is_flat == True:
  print("Be careful not to fall off!")
print("attention")

print(type(the_world_is_flat))
the_world_is_flat = 12
print(type(the_world_is_flat))

s ="L'orage gronde"
print(s)
s1 ='L\'orage gronde'
print(s1)
p = "c:\\toto\\num"
print(p)
p1 = r"c:\toto\num"
print(p1)
p2 = r'c:\toto\num'
print(p2)

s1 = "Ligne1\n"
s1 =s1+"Ligne2\n"
print(s1)

s2 = """Ligne1
Ligne2
Ligne3"""
print(s2)

a = 3
s ="a = "+str(a)
print(s)
print(50*'-')
print("toto"*12)


a = 'Py' 
'thon'

print(a)

s = "Il fait beau"
print(len(s))

print(s[5]) # doit renvoyer i
print(s[-1])

print(s[3:5])
print(s[3:])
print(s[:3])
print(s[:3]+s[3:])


s = "Python"
print(hex(id(s)))
s = "Toto"
print(hex(id(s)))
# s[0] = "J"
print(s)

a = 2
print(hex(id(a)))
a = 3
b = 3
print(hex(id(a)))
print(hex(id(b)))

print(50*'-')

squares = [1, 4, 9, 16, 25]
squares1 = squares[:]
print(squares)
print(squares[2])

squares[0] = 1000
print(squares)
print(squares1)

l1 = [
    [1,2,3], 
    [4,5,6],
    [7,8,9],
]
# l2 = l1[:] => shallow copy 
l2=copy.deepcopy(l1)
l1[1][1] = 1000
print(l1)
print(l2)
l1.append('toto')
print(l1)

print(50*'-')
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

languages = ['Python','JavaScript','Shell','Perl','C','C++','Java','SQL']

cpt=0
for i in languages:
    print(cpt,i)
    # cpt=cpt+1
    cpt+=1

for i in range(12):
    print(i)

for i in range(len(languages)):
    print(i,languages[i])
    

print(list(range(5)))
print(50*'-')
for i in languages:
    print(i)
    if i =="Perl":
        print("ok")
        break
else:
    print("ko")
    
    
a=2

if a==3:
    pass
    # utu
    
print("toto")
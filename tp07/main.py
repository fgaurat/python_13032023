import json

def main():
    d = {'name':"GAURAT","firstname":"Frédéric","age":46,"set":list({1,2,3}),"tuple":(1,2,3),"data":["titi","toto","tata"]}
    l = [d,d,d,d,d]
    # ecriture
    with open('d.json','w') as f:
        json.dump(l, f)
    
    # Lecture
    with open('d.json','r') as f:
        d = json.load(f)
        print(type(d))
        print(d[0]['name'])

def main_read():
    with open('lefichier.txt','r') as f:
        # all = f.read()
        # print(all)
        # pas_all = f.readline()
        # print(pas_all)
        # pas_all = f.readline()
        # print(pas_all)
        
        for line in f:
            print(line.strip())
def main_write():
    with open('lefichier.txt','a') as f:
        f.write("Helloooooo\n")
        print("toto",file=f)

if __name__=='__main__':
    main()


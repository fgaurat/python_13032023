
from Rectangle import Rectangle

def main():

    r = Rectangle(2,3)
    
    l = r.get_longueur()    
    print(l)
    r.set_longueur(12)
    
    l = r.get_longueur()    
    print(l) # 12
    s = r.surface()
    
    print(s)
    print(r)

if __name__=='__main__':
    main()


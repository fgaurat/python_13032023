from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle

def show_surface(o):
    print(o)
    print(o.surface())

def main():
    c = Carre(10)
    r = Rectangle(10,5)
    ce =Cercle(5)
    show_surface(c)
    show_surface(r)
    # show_surface(ce)

if __name__=='__main__':
    main()



from dataclasses import dataclass

@dataclass
class RectangleData:
    longueur:int=0
    largeur:int=0
    
    @property
    def surface(self):
        return self.longueur*self.largeur
    
          
def main():

    r = RectangleData(12,2)
    print(r)
    print(r.longueur)
    print(r.largeur)
    print(r.surface)

if __name__=='__main__':
    main()


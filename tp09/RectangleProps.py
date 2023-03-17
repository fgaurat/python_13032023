

class RectangleProps:
    
    
    def __init__(self,longueur,largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur
    
    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    def largeur(self,longueur):
        self._largeur = longueur      
    
    @property
    def surface(self):
        return   self._largeur*self._longueur
          
def main():
    r = RectangleProps(12,3)
    
    r.longueur = 12
    a = r.get_longueur()
    print(r.longueur)
    print(r.surface)
    

if __name__=='__main__':
    main()


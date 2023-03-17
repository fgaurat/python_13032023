

class Rectangle:
    
    def __init__(self,longueur,largeur):
        self._longueur = longueur
        self._largeur = largeur
        
    def get_longueur(self):
        return self._longueur
    
    def set_longueur(self,longueur):
        self._longueur = longueur
    
    def get_largeur(self):
        return self._largeur
    
    def set_largeur(self,longueur):
        self._largeur = longueur
    
    def surface(self):
        return self._longueur * self._largeur 
    
    def __str__(self):
        return f"{__class__.__name__} : {self._longueur=}, {self._largeur=},"
    
import math


from ICalcGeo import ICalcGeo

    

class Cercle(ICalcGeo):
    
    def __init__(self,rayon):
        self._rayon = rayon
    
    def get_rayon(self):
        return self._rayon
    
    def set_rayon(self,rayon):
        self._rayon = rayon
    
    # def surface(self):
    #     return math.pi*self._rayon**2
    
    
    def __str__(self):
        return f'{__class__.__name__} {self._rayon=}'

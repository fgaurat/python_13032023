from Rectangle import Rectangle

class Carre(Rectangle):
    
    def __init__(self, cote):
        super().__init__(cote, cote)
        self._cote = cote
    
    # def __str__(self):
    #     return f"{__class__.__name__} {self._cote=}"
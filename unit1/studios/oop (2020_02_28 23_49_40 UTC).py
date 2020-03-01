class Fraction:
     def __init__(self,nom,denom):
         self.nom = nom
         self.denom = denom

     def __float__(self):
         return self.nom/self.denom

    def __str__(self):
        return "Fraction([:d]

    def __add__(self,frac2):
        if isinstance(other,Fraction):
            new_denom = self.denom * frac2.denom
            new_nom = self.nom * self.frac2 + self.nom * other.denom
        elif isinstance(other, int):
            new_nom = self.denom * other + self.nom
            return Fraction(new_nom,denom)
        else:
            raise TypeError("unsupported operandus")

test_frac = Fraction(5,9)

print(float(test_frac))

print(test_frac = 

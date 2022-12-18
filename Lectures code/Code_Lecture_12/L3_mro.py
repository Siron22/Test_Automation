class R:
    pass
    def meth(self):
        print("In R")


class D(R):
    pass

class E(R):
    pass



class B(D):
    pass
    # def meth(self):
    #     print("In B")

class C(E):
    pass
    # def meth(self):
    #     print("In C")

class A(B, C):
    pass
    # def meth(self):
    #     print("In A")

"""
L(A) = A + merge(L(B), L(C), B, C) = A + merge(BDR + CER + B + C) = AB + merge(DR + CER + C) = ABD + merge(R + CER + C) = 
= ABD + merge(CER + C) = ABDC +merge(ER) = ABDCER 
L(B) = B + merge(L(D), D) = B + merge(DR, D) = B + D + R = BDR
L(C) = C + merge(L(E), E) = C + merge(ER, E) = CER
L(D) = DR
L(E) = ER
"""




a = A()
a.meth()

print(A.__mro__)

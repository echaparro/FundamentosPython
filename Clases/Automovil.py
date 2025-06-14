class Automovil :
    def __init__(self, parMarca, parColor):
        self.marca= parMarca
        self.color= parColor
    
    def Avanzar(self):
        print("El coche avanza y es un:{}".format(self.marca))
        

    def Retroceder(self):
         print("El coche Retrocede y es un:{}".format(self.marca))
    


if __name__=="__main__":
    Auto = Automovil("Toyota","Gris")
    Auto2 = Automovil("Honda","Verde")

    print(Auto.Avanzar())
    print(Auto2.Retroceder())
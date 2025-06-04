if __name__ =="__main__":

    
    def OperadoresAritmeticos(parNum1, parNum2):
        print("----- Operadores Aritmeticos -----")
        print("Operador suma: ", parNum1+parNum2)
        print("Operador resta: ", parNum1-parNum2)
        print("Operador multiplicacion: ", parNum1*parNum2)
        print("Operador division: ", parNum1/parNum2)
        
    def OperadoresComparacion(parNum1, parNum2):
        print("----- Operadores Comparación -----")
        print("Operador Mayor que: ", parNum1 > parNum2)
        print("Operador Menor que: ", parNum1 < parNum2)
        print("Operador Igual que: ", parNum1 == parNum2)
        print("Operador Menor o igual que: ", parNum1 <= parNum2)
        print("Operador Mayor o igual que: ", parNum1 >= parNum2)
        print("Operador Diferente que: ", parNum1 != parNum2)


    def TablasVerdad():
        print("----- Negación NOT-----")
        print("True : ",not True)
        print("False : ",not False)
        print("----- Conjunción AND-----")
        print("True - True :",True and True)
        print("True - False :",True and False)
        print("False - True :",False and True)
        print("False - False :",False and False)
        print("----- Disyunción OR-----")
        print("True - True :",True or True)
        print("True - False :",True or False)
        print("False - True :",False or True)
        print("False - False :",False or False)


    OperadoresAritmeticos(2,2)
    OperadoresComparacion(2,2)
    TablasVerdad()



class Pide():
    def __init__(self, letrero, li = 0, ls = 0, ciclo = "", tipo = ""):
        self.letrero = letrero
        self.li = li
        self.ls = ls
        self.ciclo = ciclo.upper()
        self.tipo = tipo

    def __del__(self):
        pass

    def error(self):
        print('\n' + " [!!!] ERROR [!!!]")
        print(" " +self.letrero + ". . . " + '\n' + " Intente de nuevo." + '\n')

    def como_cadena(self):
        if (self.ciclo == "SI") and ((self.li != 0) or (self.ls != 0)):
            while True:
                cad = input(self.letrero)
                if len(cad) < self.li or len(cad) > self.ls:
                    mensaje_error = "La cadena debe estar entre " + str(self.li) + " y " + str(self.ls) + " caracteres." 

                    # Creates an object with error message
                    mer = Pide(mensaje_error)
                    mer.error()
                    del mer
                else:
                    return cad
            # Termina ciclo
        else:
            cad = input(self.letrero)
            return cad

    def como_numero(self):
         while True:
            cad = input(self.letrero)
            if not cad.isnumeric():
                mensaje_error = "Solo deben ser digitos numéricos . . ." 
                # Creates an object with error message
                mer = Pide(mensaje_error)
                mer.error()
                del mer
            else:
                if self.tipo == "int": num = int(cad)
                else: num = float(cad)
                if (self.ls != 0 and self.li != 0 and self.ciclo == "SI"):
                    if num < self.li or num > self.ls:
                        mensaje_error =  mensaje_error = "El número debe estar entre " + str(self.li) + " y " + str(self.ls)
                        mer = Pide(mensaje_error)
                        mer.error()
                        del mer
                    else: return num
                else: return num

# Termina la clase Pide

#Pide1 = Pide("Indica tu nombre : ", ciclo = "si", li = 3, ls = 10)
#cad = Pide1.pide_cadena()
#print("Cadena =", cad)
#pn1 = Pide("Indica un número : ", tipo = "int", li = 5, ls = 10, ciclo = "si")
#x = pn1.pide_numero()
#print("x=",x)

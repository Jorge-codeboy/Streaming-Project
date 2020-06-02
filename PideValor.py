class PideValor():
    def __init__(self, letrero, li = 0, ls = 0, ciclo = "", tipo = ""):
        self.letrero = letrero
        self.li = li
        self.ls = ls
        self.ciclo = ciclo.upper()
        self.tipo = tipo

    def __del__(self):
        pass

    def error(self):
        print(self.letrero)
        input()

    def pide_cadena(self):
        if (self.ciclo == "SI") and ((self.li != 0) or (self.ls != 0)):
            while True:
                cad = input(self.letrero)
                if len(cad) < self.li or len(cad) > self.ls:
                    mensaje_error = "Error la cadena debe estar entre " + str(self.li) + " y " + str(self.ls) + " caracteres . . ." 

                    # Creates an object with error message
                    mer = PideValor(mensaje_error)
                    mer.error()
                    del mer
                else:
                    return cad
            # Termina ciclo
        else:
            cad = input(self.letrero)
            return cad

    def pide_numero(self):
         while True:
            cad = input(self.letrero)
            if not cad.isnumeric():
                mensaje_error = "Error solo deben ser digitos numéricos . . ." 
                # Creates an object with error message
                mer = PideValor(mensaje_error)
                mer.error()
                del mer
            else:
                if self.tipo == "int": num = int(cad)
                else: num = float(cad)
                if (self.ls != 0 and self.li != 0 and self.ciclo == "SI"):
                    if num < self.li or num > self.ls:
                        mensaje_error =  mensaje_error = "Error la cadena debe estar entre " + str(self.li) + " y " + str(self.ls)
                        mer = PideValor(mensaje_error)
                        mer.error()
                        del mer
                    else: return num
                else: return num

# Termina la clase PideValor

#pv1 = PideValor("Indica tu nombre : ", ciclo = "si", li = 3, ls = 10)
#cad = pv1.pide_cadena()
#print("Cadena =", cad)
#pn1 = PideValor("Indica un número : ", tipo = "int", li = 5, ls = 10, ciclo = "si")
#x = pn1.pide_numero()
#print("x=",x)

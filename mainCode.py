import validacion

class Videos():
    def __init__(self, ID, titu, dura, cali):
        self.ID  = ID
        self.titu = titu
        self.dura = dura
        self.cali = cali

    def pide_datos(self):
        self.ID = validacion.Pide("Indica el ID > ", 5, 5, "SI", "").como_cadena()
        self.titu = validacion.Pide("---Indica el titulo     > ", 1, 30, "SI", "").como_cadena()
        self.dura = validacion.Pide("---Indica la duración   > ", 1, 500, "SI", "int").como_numero()
        self.cali = validacion.Pide("---Indica la calificacion> ", 1, 5, "SI", "int").como_numero()
        print(self.ID)
        
    def muestra(self):
        if self.ID != "" and self.titu != "" and self.dura != "" and self.cali != "":
            print("ID              : ", self.ID)
            print("Titulo          : ", self.titu)
            print("Duración        : ", self.dura)
            print("Calificación    : ", self.cali)

class Peliculas(Videos):

    def __init__(self, ID, titu, dura, cali, audi, gene):
        self.audi = audi
        self.gene = gene
        super().__init__(ID, titu, dura, cali)

    def pide_datos(self):
        super().pide_datos()
        self.audi = validacion.Pide("---Indica la audiencia > ", 1, 15, "SI", "").como_cadena()
        self.gene = validacion.Pide("---Indica el género    > ", 1, 15, "SI", "").como_cadena()

    def muestra(self):
        super().muestra()
        if self.audi != "" and self.gene != "":
            print("Audiencia       : ", self.audi)
            print("Género          : ", self.gene)

class Serie(Peliculas):

    def __init__(self, ID, titu, dura, cali, audi, gene, temp, epis, titE):
        self.temp = temp
        self.epis = epis
        self.titE = titE
        super().__init__(ID, titu, dura, cali, audi, gene)

    def pide_datos(self):
        super().pide_datos()
        self.temp = validacion.Pide("---Indica la temporada: ", 1, 500, "SI","int").como_numero()
        self.epis = validacion.Pide("---Indica el episodio : ", 1, 500, "SI","int").como_numero()
        self.titE = validacion.Pide("---Indica el título del episodio ", 1, 30,"SI","").como_cadena()

    def muestra(self):
        super().muestra()
        if self.temp != "" and self.epis != "" and self.titE != "":
            print("Temporada       : ", self.temp)
            print("No. Episodio    : ", self.epis)
            print("Título Episodio : ", self.titE)



class Documental(Serie):

    def __init__(self, ID, titu, dura, cali, audi, gene, temp, epis, titE, tema):
        self.tema = tema
        super().__init__(ID, titu, dura, cali, audi, gene, temp, epis, titE)

    def pide_datos(self):
        super().pide_datos()
        self.tema = validacion.Pide("---Indica el tema ", 1, 30, "SI", "").como_cadena()

    def muestra(self):
        super().muestra()
        if  self.tema != "":
            print("Tema            : ", self.tema)

    


d = Documental("", "", "", "", "", "", "", "", "", "")
d.pide_datos()
d.muestra()


# By ANTONIMOUS

#print('{:.5}'.format('aaabbbccc'))






















'''






class Archivo():

    def __init__(self):
        pass

    def busca(self):
        pass

    def graba(self):
        pass


class Listados():
    def __init__(self):
        pass



    def general(self):
        pass


'''

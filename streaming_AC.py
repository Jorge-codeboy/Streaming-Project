import validacion

class Videos():
    def __init__(self, ID, titu, dura, cali, gene):
        self.ID  = ID
        self.titu = titu
        self.dura = dura
        self.cali = cali
        self.gene = gene

    def pide_datos(self):
        while True:
            ID = validacion.Pide("Indica el ID > ", 5, 5, "SI", "").como_cadena()
            ID = ID.upper()
            if ID[0] != "P" and ID[0] != "D" and ID[0] != "S":
                validacion.Pide("Solo puede iniciar con P (Películas), S (Series) o D (Documentales)").error()
            elif ID[1] != "A" and ID[1] != "B" and ID[1] != "C" and ID[1] != "D":
                validacion.Pide("La segunda letra solo puede ser A (Apto para Todos), B (Adolescentes y Adultos) o C (Solo Adulos) o D (Adultos de Alto Criterio)").error()
            elif (ID[2:6].isnumeric() == False):
                validacion.Pide("A partir del tercer dígito solo es válido números").error()
            else:
                self.ID = ID
                break

        self.titu = validacion.Pide("---Indica el titulo     > ", 1, 30, "SI", "").como_cadena()
        self.dura = validacion.Pide("---Indica la duración   > ", 1, 500, "SI", "int").como_numero()
        self.cali = validacion.Pide("---Indica la calificacion > ", 1, 5, "SI", "int").como_numero()

    def muestra(self):
        if self.ID != "" and self.titu != "" and self.dura != "" and self.cali != "":
            print("ID              : ", self.ID)
            print("Titulo          : ", self.titu)
            print("Duración        : ", self.dura)
            print("Calificación    : ", self.cali)

    def __str__(self):
        
        cad = self.ID +","+ self.titu +"," + str(self.gene).strip() + "," + str(self.dura).strip() +","+ str(self.cali).strip() + ","

        return(cad)

class Peliculas(Videos):

    def __init__(self, ID, titu, dura, cali, audi, gene):
        self.audi = audi
        self.gene = gene
        super().__init__(ID, titu, dura, cali, gene)

    def pide_datos(self):
        super().pide_datos()
        if self.ID[0] == "P":
            self.audi = validacion.Pide("---Indica la audiencia > ", 1, 15, "SI", "").como_cadena()
            self.gene = validacion.Pide("---Indica el género    > ", 1, 15, "SI", "").como_cadena()

    def muestra(self):
        super().muestra()
        if self.audi != "" and self.gene != "":
            print("Audiencia       : ", self.audi)
            print("Género          : ", self.gene)

    def __str__(self):

        cad= self.audi + ","

        
        return (super().__str__()+cad)

class Serie(Peliculas):

    def __init__(self, ID, titu, dura, cali, audi, gene, temp, epis, titE):
        self.temp = temp
        self.epis = epis
        self.titE = titE
        super().__init__(ID, titu, dura, cali, audi, gene)

    def pide_datos(self):
        super().pide_datos()
        if self.ID[0] == "S":
            self.temp = validacion.Pide("---Indica la temporada > ", 1, 500, "SI","int").como_numero()
            self.epis = validacion.Pide("---Indica el episodio > ", 1, 500, "SI","int").como_numero()
            self.titE = validacion.Pide("---Indica el título del episodio > ", 1, 30,"SI","").como_cadena()

    def muestra(self):
        super().muestra()
        if self.temp != "" and self.epis != "" and self.titE != "":
            print("Temporada       : ", self.temp)
            print("No. Episodio    : ", self.epis)
            print("Título Episodio : ", self.titE)

    def __str__(self):

        cad= str(self.temp).strip() + "," + str(self.epis).strip() + "," + self.titE + ","

        
        return (super().__str__()+cad)

class Documental(Serie):

    def __init__(self, ID, titu, dura, cali, audi, gene, temp, epis, titE, tema):
        self.tema = tema
        super().__init__(ID, titu, dura, cali, audi, gene, temp, epis, titE)

    def pide_datos(self):
        super().pide_datos()
        if self.ID[0] == "D":
            self.tema = validacion.Pide("---Indica el tema > ", 1, 30, "SI", "").como_cadena()

    def muestra(self):
        super().muestra()
        if  self.tema != "":
            print("Tema            : ", self.tema)

    def __str__(self):

        cad= self.tema + ","
        
        return (super().__str__()+cad)  



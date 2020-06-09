import pide_valor 

class Videos():
    def __init__(self,ID,titulo,duracion,calif):

        self.ID = ID
        self.titulo = titulo
        self.duracion = duracion
        self.calif = calif
        
    def muestra(self):

        print("ID              : ",self.ID)
        print("Titulo          : ",self.titulo)
        print("Duración        : ",self.duracion)
        print("Calificación    : ",self.calif)

    def pide_datos(self):
        
        ID = pide_valor.Pide("Indica el ID : ",0,5,"SI","").como_cadena()
        titulo = pide_valor.Pide(" indica el titulo : ",0,30,"SI","").como_cadena()



'''
      
        

        Pide = Pide(" indica la duración : ",1,500,"SI","")
        duracion = Pide.pide_numero()

    
        Pide = Pide(" indica la calificacion : ",1,5,"SI","")
        calificacion = Pide.pide_numero()

class Peliculas(Videos):

    def __init__(self, ID, titulo, duracion, calif,audiencia,genero):
        super().__init__(ID, titulo, duracion, calif)


        self.audiencia = audiencia
        self.genero = genero

    def muestra(self):
        super().muestra()

        if self.audiencia != "" and self.genero !="":
            print("Audiencia       : ",self.audiencia)
            print("Genero          : ",self.genero)

    def pide_datos(self):
        return super().pide_datos()

        Pide = Pide(" indica la audiencia : ",0,15,"SI","")
        audiencia = Pide.pide_cadena()

        Pide = Pide(" indica el género : ",0,15,"SI","")
        genero = Pide.pide_cadena()        
        
class Serie(Peliculas):

    def __init__(self, ID, titulo, duracion, calif, audiencia, genero,temporada,ep,tit_ep):
        super().__init__(ID, titulo, duracion, calif, audiencia, genero)


        self.temporada = temporada
        self.ep = ep
        self.tit_ep = tit_ep

    def muestra(self):
        super().muestra()

        if self.temporada != "" and self.tit_ep !="" and tit_ep != "":
            print("temporada       : ",self.temporada)
            print("ep              : ",self.ep)
            print("Título Episodio : ",self.ep)

    def pide_datos(self):
        return super().pide_datos()

        ep = Pide.pide_numero(" indica el episodio : ",15,500,"SI","")

        Pide = Pide.pide_numero(" indica la temporada: ",1,500,"SI","")
        temporada = Pide.pide_numero()       

        Pide = Pide.pide_numero(" indica el título del episodio ",1,30,"SI","")
        tit_ep = Pide.pide_numero()  


class Documental(Serie):

    def __init__(self, ID, titulo, duracion, calif, audiencia, genero, temporada, ep, tit_ep,tema):
        super().__init__(ID, titulo, duracion, calif, audiencia, genero, temporada, ep, tit_ep)

        self.tema = tema

    def muestra(self):
        super().muestra()

        if  self.tema !="":
            print("Tema         : ",self.tema)

    def pide_datos(self):
        return super().pide_datos()
        Pide = Pide(" indica el tema ",1,30,"SI","")
        tema = Pide.pide_numero()  

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
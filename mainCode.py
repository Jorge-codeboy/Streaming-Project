from PideValor import PideValor as PV

class Video():

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
        pv = PV(" indica el ID : ",0,5,"SI","")
        ID = pv.pide_cadena()


        pv = PV(" indica el titulo : ",0,30,"SI","")
        titulo = pv.pide_cadena()

        pv = PV(" indica la duración : ",1,500,"SI","")
        duracion = pv.pide_numero()

    
        pv = PV(" indica la calificacion : ",1,5,"SI","")
        calificacion = pv.pide_numero()
              

class Pelicula(Video):

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

        pv = PV(" indica la audiencia : ",0,15,"SI","")
        audiencia = pv.pide_cadena()

        pv = PV(" indica el género : ",0,15,"SI","")
        genero = pv.pide_cadena()        
        

class Serie(Pelicula):

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

        pv = PV(" indica el episodio : ",15,500,"SI","")
        ep = pv.pide_numero()     

        pv = PV(" indica la temporada: ",1,500,"SI","")
        temporada = pv.pide_numero()       

        pv = PV(" indica el título del episodio ",1,30,"SI","")
        tit_ep = pv.pide_numero()  
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
        pv = PV(" indica el tema ",1,30,"SI","")
        tema = pv.pide_numero()  

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



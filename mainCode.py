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
class Documental(Serie):

    def __init__(self, ID, titulo, duracion, calif, audiencia, genero, temporada, ep, tit_ep,tema):
        super().__init__(ID, titulo, duracion, calif, audiencia, genero, temporada, ep, tit_ep)

        self.tema = tema

    def muestra(self):
        super().muestra()

        if  self.tema !="":
            print("Tema         : ",self.tema)


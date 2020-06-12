import csv
from csv import reader

class Archivo():
    def __init__(self):
        self.videos = []

    def cargar_csv(self, archivo):
        
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.videos.append(row)
                
        
    def graba(self, video, archivo):
        
        arr = video.split(",")
        self.videos.append(arr)




        with open(str(archivo), 'w', newline="") as file:
            writer = csv.writer(file)
            for videos in self.videos:
                writer.writerow(videos)

    def busca(self, atributo):
        vid = []
        bandera_existe = False
        for video in self.videos:

            if atributo in video[0]:
                bandera_existe=True
                
                vid = video
                break
        return(bandera_existe,vid)

        
class Listados():

    def __init__(self, videos):
        self.videos = videos
        
    def general(self, valor_a_buscar, posicion, li = 0, ls = 0):

        x=range(li,ls+1)
        
        # Posicion 0, ID
        # Posicion 1, Título
        # Posicion 2, Género
        # Posicion 3, Duración
        # Posicion 4, Calificación
        # Posicion 5, Audiencia
        # Posicion 6, Temporada
        # Posicion 7, No. Episodio
        # Posicion 8, Tit. Episodio
        # Posicion 9, Tema

        ls = []
        bandera_existe = False

        if valor_a_buscar == "" and li != 0 and ls != 0:

            for vid in self.videos:
                try:
                    if  int(vid[4]) in x:
                        ls.append(vid)
                        bandera_existe =True
                except:
                    pass

            return(bandera_existe, ls)


        for vid in self.videos:
            finder = (vid[posicion]).find(valor_a_buscar)
            if finder == 0:
                ls.append(vid)
                bandera_existe = True
        return(bandera_existe, ls)

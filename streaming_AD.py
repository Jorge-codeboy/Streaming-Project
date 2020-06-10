import csv
from csv import reader

class archivo():
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

    def busca(self, video_a_buscar, posicion):
        # Posicion 0, ID
        # Posicion 1, Título
        # Posicion 2, Duración
        # Posicion 3, Calificación
        # Posicion 4, Audiencia
        # Posicion 5, Género
        # Posicion 6, Temporada
        # Posicion 7, No. Episodio
        # Posicion 8, Tit. Episodio
        # Posicion 9, Tema

        bandera_existe = False

        for video in self.videos:
            if video_a_buscar in video[posicion]:    
                bandera_existe = True
                break
        return(bandera_existe)

        


      



            








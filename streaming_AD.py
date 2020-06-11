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

    # def busca(self, video_a_buscar, posicion):
    #     # Posicion 0, ID
    #     # Posicion 1, Título
    #     # Posicion 2, Duración
    #     # Posicion 3, Calificación
    #     # Posicion 4, Audiencia
    #     # Posicion 5, Género
    #     # Posicion 6, Temporada
    #     # Posicion 7, No. Episodio
    #     # Posicion 8, Tit. Episodio
    #     # Posicion 9, Tema

    #     bandera_existe = False

    #     for video in self.videos:
    #         if video_a_buscar in video[posicion]:    
    #             bandera_existe = True
    #             break
    #     return(bandera_existe)

    def busca(self, atributo, posicion):

        
        # Posicion 0, ID
        # Posicion 1, Título
        # Posicion 2, género
        # Posicion 3, Duración
        # Posicion 4, Calificación
        # Posicion 5, Audiencia
        # Posicion 6, Temporada
        # Posicion 7, No. Episodio
        # Posicion 8, Tit. Episodio
        # Posicion 9, Tema

        bandera_existe = False

        if posicion == 0:
            vid = []

            for video in self.videos:

                if atributo in video[0]:
                    bandera_existe=True
                    
                    vid = video
                    break

                    
            return(bandera_existe,vid)
                


            

        else:

            for video in self.videos:

                try:

                    if atributo in video[posicion]:    
                        print(video)
                        bandera_existe=True
                        

                        

                except:
                    pass

            

                
            return(bandera_existe)
    

        
class Listados():

    def __init__(self, videos):

        self.videos = videos
        
        

    def general(self, tipo, ci,cs):
        

        


        if tipo == "general":

            



            for video in self.videos:

                try:

                    if "P" in video[0] or "S" in video[0] or "D" in video[0]:    
                        print(video)
                        
                        

                except:
                    pass
            
        if tipo == "peliculas" :



           

            for video in self.videos:
                print(video)

                 
                try:

                    if "P" in video[0]:    
                        print(video)
                        

                except:
                    pass
                

        if tipo == "series":

            for video in self.videos:

                try:

                    if "S" in video[0]:    
                        print(video)
                        

                except:
                    pass

        if tipo == "documentales":

            for video in self.videos:

                try:

                    if "D" in video[0]:    
                        print(video)

                        


                        

                except:
                    pass
        if tipo == "calificaciones":

            for video in self.videos:

                x = range(ci,cs+1)
                

                try:


                    if  int(video[4]) in x:

                        print(video)
                        

                except:
                    pass

      



            








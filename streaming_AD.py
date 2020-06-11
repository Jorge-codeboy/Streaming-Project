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
                        vid=video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]
                        bandera_existe=True
                        

                        

                except:
                    pass

            

                
            return(bandera_existe,vid)
    

        
class Listados():

    def __init__(self, videos):

        self.videos = videos
        
        

    def general(self, tipo, p1,p2):
        vids=[]
        bandera_existe = False

        if tipo == "consulta_l":

            for video in self.videos:

                try:

                    if p1 in video[p2]:    
                        vid="["+video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]+"]"
                        bandera_existe=True
                        vids.append(vid)

                        

                except:
                    pass

            

                
            return(bandera_existe,vids)
        

        


        if tipo == "general":

            



            for video in self.videos:

                try:

                    if "P" in video[0] or "S" in video[0] or "D" in video[0]:    
                        vid="["+video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]+"]"
                        vids.append(vid)
                        
                        

                except:
                    pass

            return(vids)

                
            
        if tipo == "peliculas" :



           

            for video in self.videos:
                

                 
                try:

                    if "P" in video[0][0]:

                        vid="["+video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]+"]"
                        vids.append(vid)
                        

                except:
                    pass

            return(vids)    

        if tipo == "series":

            for video in self.videos:

                try:

                    if "S" in video[0]:    


                        vid="["+video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]+"]"
                        vids.append(vid)
                except:
                    pass
            return(vids)

        if tipo == "documentales":

            for video in self.videos:

                try:

                    if "D" in video[0][0]:    
                        vid="["+video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]+"]"
                        vids.append(vid)
                        


                        

                except:
                    pass
            return(vids)
        if tipo == "calificaciones":

            for video in self.videos:

                x = range(p1,p2+1)
                

                try:


                    if  int(video[4]) in x:
                        vid="["+video[0]+","+video[1][0:16]+","+video[2]+","+video[3]+","+video[4]+","+video[5]+","+video[6]+","+video[7]+","+video[8]+","+video[9][0:16]+"]"
                        vids.append(vid)

                except:
                    pass
            return(vids)
      



            








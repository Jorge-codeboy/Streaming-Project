import csv
from csv import reader

class lista_videos_AD():


    videos =[]

    def cargar_archivo(self):
        with open('videos.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:

                self.videos.append(row)

    def grabar_video(self,video):

        self.videos.append(video)

        with open('videos.csv', 'w', newline="") as file:
            writer = csv.writer(file)

            for video in self.videos:

                writer.writerow(video)

    def existe_video(self,video):

        bandera_existe = False

        with open('videos.csv', 'r') as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0]==video[0]:
                    bandera_existe = True

        return(bandera_existe)





        


      



            








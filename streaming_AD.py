import csv
from csv import reader

class archivo():


    videos =[]

    def cargar_archivo(self):
        with open('videos.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:

                self.videos.append(row)

    def graba(self,video):

        self.videos.append(video)

        with open('videos.csv', 'w', newline="") as file:
            writer = csv.writer(file)

            for video in self.videos:

                writer.writerow(video)

    def busca(self,atributo):

        

        bandera_existe = False


        for video in self.videos:

            index = 1

            if atributo in video:
                bandera_existe= True
                index == self.videos.index(video)
                print(video)






        return(bandera_existe)



archivo().busca("blanca")

        


      



            








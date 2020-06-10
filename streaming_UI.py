import validacion

import streaming_AD as ad

#import mainCode as mc

import winsound as ws

class listados():

    def menu(self):

        while True:
            ws.PlaySound("somebody", ws.SND_ASYNC)

            print('''
###############################################
             __     _    __ _ _       
          /\ \ \___| |_ / _| (_)_  __ 
         /  \/ / _ \ __| |_| | \ \/ / 
        / /\  /  __/ |_|  _| | |>  <  
        \_\ \/ \___|\__|_| |_|_/_/\_\ 
                              
    1) Agregar Videos
    2) Consultar Video por ID

    -- R E P O R T E S --

    3) Consultar Video por Título
    4) Consultar Video por Género
    5) Listado General
    6) Listado de Películas
    7) Listado de Series
    8) Listado de Documentales
    9) Listado por Calificaciones
    10) Salir

############################################### ''')

        
            op = validacion.Pide('\n' + "Tu opción > ", 1, 10,"SI","int").como_numero()
            return op

            

    def agrega_video(self):

        op = 0

        while op !=4:

            print("1) agregar pelicula")
            print("2) agregar serie")
            print("3) agregar Documental")
            print("4) salir")

            op= validacion.Pide("Indica la opción deseada",1,4,"int").como_numero()

            if op ==1:
                pass

            if op ==2:
                pass

            if op ==3:
                pass
    
        pass

    def consulta_ID(self):
        
        pass

    def consulta_titulo(self):
        
        pass

    def consulta_genero(self):
        
        pass

    def listado_general(self):
        
        pass

    def listado_peliculas(self):
        
        pass

    def listado_series(self):
        
        pass

    def listado_documentales(self):
        
        pass

    def listado_calificaciones(self):
        
        pass


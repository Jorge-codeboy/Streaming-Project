import os
import time
import validacion
import winsound as ws
import streaming_AD as ad
import streaming_AC as ac


class listados():

    def __init__(self):
        pass

    def menu(self):

        while True:
            
            ws.PlaySound("somebody", ws.SND_ASYNC)
            os.system('cls')

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

            if op == 1:
                self.agrega_video()
            else:
                quit()

    def agrega_video(self):

        arch = ad.archivo()
        arch.cargar_csv("testFile.csv")
        video = ac.Documental("", "", "", "", "", "", "", "", "", "")
        video.pide_datos()
        existe = arch.busca(video.ID, 0)

        if not existe:
            op =validacion.Pide('\n' + " [¿¿¿] ESTÁ SEGURO QUE DESEA AÑADIR " + str(video.ID) + " [???] " +
            '\n' + "    1 PARA ACEPTAR | 0 PARA ABORTAR" + '\n' + "> ", 0, 1, "", "int").como_numero()
            
            if op == 1:
                video_str = str(video)
                print(video_str)
                arch.graba(video_str, "testFile.csv")
                os.system("cls")
                print('''
               \|/ ____ \|/       
                @~/ .. \~@        
               /_( \__/ )_\      ¡ R E G I S T R O   E X I T O S O !
                  \____/    
                ''')
                time.sleep(2.5)
        else:
            validacion.Pide("El ID se duplica en la base de datos").error()
            print(" VOLVIENDO AL MENÚ PRINCIPAL . . .")
            time.sleep(2.5)


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


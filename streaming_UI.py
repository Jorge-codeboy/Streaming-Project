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
            
            #ws.PlaySound("somebody", ws.SND_ASYNC)
            #os.system('cls')

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
                print("TERMINE")

            elif op == 2:
                ID = validacion.Pide("indica ID : ",5,5,"SI","").como_cadena()

                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
                print("################################################################")
                print("#__________________________CONSULTA POR ID_____________________#")
                print("################################################################","\n") 
                bandera,vid = arch.busca(ID,0)

                if bandera == False:
                    print("no hay video con ese ID")
                else:
                    
                    video = ac.Documental(vid[0],vid[1],vid[3],vid[4],vid[5],vid[2],vid[6],vid[7],vid[8],vid[9])

                    video.muestra()


            elif op == 3:
                        
                titulo = validacion.Pide("indica titulo : ",1,30,"SI","").como_cadena()

                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")

                print("####################################################################")
                print("#__________________________CONSULTA POR TÍTULO_____________________#")
                print("####################################################################","\n")               


                bandera,videos = ad.Listados(arch.videos).general("consulta_l",titulo,1)

                if bandera == False:
                    print("no hay video con ese titulo : ")

                else:
                    for vid in videos:
                        print (vid)

                

            elif op == 4:
                genero = validacion.Pide("indica genero : ",1,15,"SI","").como_cadena()

                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
                print("####################################################################")
                print("#__________________________CONSULTA POR GÉNERO_____________________#")
                print("####################################################################","\n")               

                bandera,videos = ad.Listados(arch.videos).general("consulta_l",genero,2)

                if bandera == False:
                    print("no hay video con ese genero")

                else:
                    for vid in videos:
                        print (vid)                    
            elif op == 5:
                print("################################################################")
                print("#__________________________LISTADO GENERAL_____________________#")
                print("################################################################","\n")
                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
        
                videos =ad.Listados(arch.videos).general("general","","")

                for vid in videos:
                    print(vid)
            elif op == 6:
                print("#####################################################################")
                print("#__________________________LISTADO DE PELICULAS_____________________#")
                print("#####################################################################","\n")
                
                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
        
                videos = ad.Listados(arch.videos).general("peliculas","","")
                

                for vid in videos:
                    print(vid)                
            elif op == 7:
                print("###############################################################")
                print("#__________________________LISTADO SERIES_____________________#")
                print("###############################################################","\n")
                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
        
                videos =ad.Listados(arch.videos).general("series","","")

                for vid in videos:
                    print(vid)                    

            elif op == 8:
                print("#####################################################################")
                print("#__________________________LISTADO DOCUMENTALES_____________________#")
                print("#####################################################################","\n")
                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
        
                videos = ad.Listados(arch.videos).general("documentales","","")
                for vid in videos:
                    print(vid)    

            elif op == 9:

                cali_i = validacion.Pide("indica limite inferior de calificación : ",1,5,"SI","int").como_numero()
                cali_s = validacion.Pide("indica limite superior de calificación : ",1,5,"SI","int").como_numero()

                arch = ad.archivo()
                arch.cargar_csv("testFile.csv")
                print("#########################################################################")
                print("#__________________________LISTADO POR CALIFICACIÓN_____________________#")
                print("#########################################################################","\n")
        
                videos = ad.Listados(arch.videos).general("calificaciones",cali_i,cali_s)                
                for vid in videos:
                    print(vid)    
            elif op == 10:
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

 




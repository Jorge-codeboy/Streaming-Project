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
            
            ws.PlaySound("netflix", ws.SND_ASYNC)
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
            os.system('cls')

            if op == 1:
                arch = ad.Archivo()
                arch.cargar_csv("videos.csv")
                video = ac.Documental("", "", "", "", "", "", "", "", "", "")
                video.pide_datos()
                existe,vid = arch.busca(video.ID)

                if not existe:
                    op =validacion.Pide('\n' + " [¿¿¿] ESTÁ SEGURO QUE DESEA AÑADIR " + str(video.ID) + " [???] " +
                    '\n' + "    1 PARA ACEPTAR | 0 PARA ABORTAR" + '\n' + "> ", 0, 1, "", "int").como_numero()
                    
                    if op == 1:

                        video_str = str(video)
                        arch.graba(video_str, "videos.csv")
                        os.system("cls")
                        ws.PlaySound("arreLulu", ws.SND_ASYNC)

                        print('''
                        \|/ ____ \|/       
                         @~/ .. \~@        
                        /_( \__/ )_\      ¡ R E G I S T R O   E X I T O S O !
                           \____/    
                        ''')
                        time.sleep(4)
                else:
                    validacion.Pide("El ID se duplica en la base de datos").error()
                    input("[ENTER] para continuar")                                                      

            elif op == 2:
                ID = validacion.Pide("---Indica ID > ",5,5,"SI","").como_cadena()
                ID = ID.upper()

                arch = ad.Archivo()
                arch.cargar_csv("videos.csv")
                bandera,vid = arch.busca(ID)

                if bandera == False:
                    validacion.Pide("No existe video con ese ID").error()
                else:
                    
                    video = ac.Documental(vid[0],vid[1],vid[3],vid[4],vid[5],vid[2],vid[6],vid[7],vid[8],vid[9])
                    print('\n' + "#"*50 + "\n")
                    video.muestra()
                print('\n' + "#"*50 + "\n")
                input("[ENTER] Para continuar.")

            elif op == 3 or op == 4:
                valor_a_buscar = ""
                posicion = 0

                if op == 3: 
                    valor_a_buscar = "título"
                    posicion = 1
                elif op == 4:
                    valor_a_buscar = "género"
                    posicion = 2
       
                valor_a_buscar = validacion.Pide("Indica " + str(valor_a_buscar) + " > ",1, 30, "SI", "").como_cadena()

                if valor_a_buscar == "Shrek":
                    ws.PlaySound("somebody", ws.SND_ASYNC)

                arch = ad.Archivo()
                arch.cargar_csv("videos.csv")
                bandera,videos = ad.Listados(arch.videos).general(valor_a_buscar, posicion)
                
                if bandera == False:
                    validacion.Pide("No existe video con ese Título").error()

                else:
                        sentence = ""
                        print(" ID    TÍTULO           DUR CAL GÉNERO           AUDIENCIA        TEMP/EPIS TIT.EPISODIO     TEMA             ")
                        print("--------------------------------------------------------------------------------------------------------------")
                        for vid in videos:
                            sentence +=  " " + vid[0] + " " + vid[1][0:16] + (16-len(vid[1]))*" " + " " + vid[3] + ((3-len(vid[3]))*" ") + "  " + \
                            vid[4] +  "  " + vid[2][0:16] + (16-len(vid[2]))*" " + " " + vid[5][0:16] + (16-len(vid[5]))*" " + " " + \
                            vid[6] + (4-len(vid[6]))*" " + "/" + vid[7] + (4-len(vid[7]))*" " + " " + vid[8][0:16] + (16-len(vid[8]))*" " + " " + \
                            vid[9][0:16] + (16-len(vid[9]))*" " + " " + '\n'    
                         
                        print(sentence)
                print('\n' + "#"*52 + "\n")
                input("[ENTER] Para continuar.")

            elif op == 5 or op == 6 or op == 7 or op == 8:
                valor_a_buscar = ""
                if op == 5: valor_a_buscar = ""
                elif op == 6: valor_a_buscar = "P"
                elif op == 7: valor_a_buscar = "S"
                elif op == 8: valor_a_buscar = "D"
                
                arch = ad.Archivo()
                arch.cargar_csv("videos.csv")
                bandera,videos = ad.Listados(arch.videos).general(valor_a_buscar, 0)
                
                if bandera == False:
                    validacion.Pide("No hay registros").error()

                else:
                        sentence = ""
                        print(" ID    TÍTULO           DUR CAL GÉNERO           AUDIENCIA        TEMP/EPIS TIT.EPISODIO     TEMA             ")
                        print("--------------------------------------------------------------------------------------------------------------")
                        for vid in videos:
                            sentence +=  " " + vid[0] + " " + vid[1][0:16] + (16-len(vid[1]))*" " + " " + vid[3] + ((3-len(vid[3]))*" ") + "  " + \
                            vid[4] +  "  " + vid[2][0:16] + (16-len(vid[2]))*" " + " " + vid[5][0:16] + (16-len(vid[5]))*" " + " " + \
                            vid[6] + (4-len(vid[6]))*" " + "/" + vid[7] + (4-len(vid[7]))*" " + " " + vid[8][0:16] + (16-len(vid[8]))*" " + " " + \
                            vid[9][0:16] + (16-len(vid[9]))*" " + " " + '\n'     
                        print(sentence)
                print('\n' + "#"*52 + "\n")
                input("[ENTER] Para continuar.")
            
            elif op == 9:

                cali_i = validacion.Pide("indica limite inferior de calificación : ",1,5,"SI","int").como_numero()
                cali_s = validacion.Pide("indica limite superior de calificación : ",1,5,"SI","int").como_numero()

                

                arch = ad.Archivo()
                arch.cargar_csv("videos.csv")
                bandera,videos = ad.Listados(arch.videos).general("", 4,cali_i,cali_s)
                
                if bandera == False:
                    validacion.Pide("No hay registros").error()

                else:
                        sentence = ""
                        print(" ID    TÍTULO           DUR CAL GÉNERO           AUDIENCIA        TEMP/EPIS TIT.EPISODIO     TEMA             ")
                        print("--------------------------------------------------------------------------------------------------------------")
                        for vid in videos:
                            sentence +=  " " + vid[0] + " " + vid[1][0:16] + (16-len(vid[1]))*" " + " " + vid[3] + ((3-len(vid[3]))*" ") + "  " + \
                            vid[4] +  "  " + vid[2][0:16] + (16-len(vid[2]))*" " + " " + vid[5][0:16] + (16-len(vid[5]))*" " + " " + \
                            vid[6] + (4-len(vid[6]))*" " + "/" + vid[7] + (4-len(vid[7]))*" " + " " + vid[8][0:16] + (16-len(vid[8]))*" " + " " + \
                            vid[9][0:16] + (16-len(vid[9]))*" " + " " + '\n'     
                        print(sentence)
                print('\n' + "#"*52 + "\n")
                input("[ENTER] Para continuar.")

  
            elif op == 10:
                quit()

  

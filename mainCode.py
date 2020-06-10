import os
import time
import validacion
import streaming_DP as dp
import streaming_UI as ui
import streaming_AD as ad

quedarse = True

while quedarse:
    
    os.system("cls")
    
    op = ui.listados().menu()
    arch = ad.archivo()
    arch.cargar_csv("testFile.csv")
    
    if op == 1:
        video = dp.Documental("", "", "", "", "", "", "", "", "", "")
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

    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        pass
    elif op == 9:
        pass
    else:
        quedarse = False

# By ANTONIMOUS

#print('{:.5}'.format('aaabbbccc'))



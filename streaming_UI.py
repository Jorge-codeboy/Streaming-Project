from PideValor import PideValor as PV

class lista_alumnos_UI:
    
    def menu():
        print("1) agregar videos")
        print("2) consulta por ID")
        print("3) consulta por Título")
        print("4) consulta por género")
        print("5) Listado general")
        print("6) Listado de películas")
        print("7) Listado de Series")
        print("8) Listado de Documentales")
        print("9) Listado por calificaciones")
        print("10) Salir")


        pv= PV("Indica la opción deseada",1,10,"int")
        op = pv.pide_numero()
        
        return(op)

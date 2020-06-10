import validacion

import streaming_AD as ad

import mainCode as mc


class listados():
    
    def menu(self):

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


        Pide= validacion.Pide("Indica la opción deseada",1,10,"int")
        op = Pide.como_numero()

        return(op)

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
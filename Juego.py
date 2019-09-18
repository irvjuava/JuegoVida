from Vida import SoporteVida

class Juego:

    def __init__( self, rows, cols ):
        self.__tablero = SoporteVida( rows, cols )
        self.__contador = 1

    def configure( self, inicial, generaciones ):
        self.__tablero.configure( inicial, generaciones )

    def to_string( self ):
        self.__tablero.to_string()
    
    def get_gens( self ):
        return self.__tablero.get_gens()

    # Esta función tiene como parámetros las coordenadas de una célula y
    # regresará un booleano representando si vive o muere para la siguiente gen
    def reglas( self, row, col ):
        vecinos = self.__tablero.get_alive_neighbors( row, col )
        if( self.__tablero.is_alive_cell( row, col )):
            if( vecinos == 2 or vecinos == 3):
                return True
            else:
                return False
        else:
            if( vecinos == 3):
                return True
            else:
                return False

    # Esta función itera en cada una de las celdas del tablero, evalúa si viven
    # o mueren y regresa el arreglo listo para ingresar en "configure"
    def checarReglas( self ):
        nuevaConfig = []
        for i in range( self.__tablero.get_num_rows() ):
            for j in range( self.__tablero.get_num_cols() ):
                if(self.reglas( i, j )):
                    tupla = [i, j]
                    nuevaConfig.append(tupla)
        return nuevaConfig

    def iterarGeneracion( self ):
        if( self.__tablero.get_gens() > 1):
            self.__contador += 1
            arregloNuevaGen = self.checarReglas()
            self.__tablero.set_gens( self.__tablero.get_gens() -1 )
            self.__tablero.configure( arregloNuevaGen,  self.__tablero.get_gens())
            print(f"-------- {self.__contador}° Generación --------")
            self.to_string()
            self.iterarGeneracion()
    
def main():
    part1 = Juego( 5, 5 )
    part1.configure( [[1,2],[2,1],[2,2],[2,3]], 20 )
    print("-------- 1° Generación --------")
    part1.to_string()
    part1.iterarGeneracion()

main()

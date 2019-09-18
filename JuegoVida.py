# JuegoVida

from Array2D import Array2D

class SoporteVida:
    def __init__( self, rows, cols ):
        self.__rows = rows
        self.__cols = cols
        self.__grid = Array2D( rows, cols )
        self.__grid.clearing(0)

    def to_string( self ):
        self.__grid.to_string()

    def get_num_rows( self ):
        return self.__rows

    def get_num_cols( self ):
        return self.__cols

    def get_gens( self ):
        return self.__gens

    def set_gens( self, generacion ):
        self.__gens = generacion

    # Inicial es una lista de la forma = [[0,0], [0,1], [3,4]]
    def configure( self, inicial, generaciones ):
        self.__grid.clearing(0)
        self.__gens = generaciones
        for cell in inicial:
            self.__grid.set_item( cell[0], cell[1], 1)

    def clear_cell( self, row, col ):
        self.__grid.set_item( row, col, 0 )

    def set_cell( self, cell, row ):
        self.__grid.set_item( row, col, 1 )

    def is_alive_cell( self, row, col ):
        return self.__grid.get_item( row, col ) == 1

    def get_alive_neighbors( self, row,col ):
        contador = 0
        x = row - 1
        y = col - 1
        for i in range(3):
            for j in range(3):
                if(0 <= x and x <= (self.get_num_rows() - 1) and 0 <= y and y <= (self.get_num_cols() - 1)):
                    if( self.is_alive_cell( x, y )):
                        contador += 1
                x += 1
            x = row - 1
            y += 1
        if(self.is_alive_cell( row, col )):
            contador -= 1
        return contador

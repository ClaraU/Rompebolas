'''
Created on 19/3/2015

@author: Clara
'''

from random import randint

class Tablero:
         
    matrizTablero = []

    def __init__(self, colores, tipo):
        self.colores = colores
        self.tipo = tipo

    def getTableroNuevo(self): 
        filas = 9
        columnas = 9   
        matrizTablero = []

        if self.tipo == 'G':          
            for i in range(filas):
                matrizTablero.append([])
                for j in range(columnas):
                     matrizTablero[i].append(randint(1, self.colores))        
                
            return matrizTablero

        elif self.tipo == 'C':            
            for i in range(filas):
                if i==0  or i==8:
                    matrizTablero.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
                elif i==1  or i==7:
                    matrizTablero.append([1, 2, 2, 2, 2, 2, 2, 2, 1])      
                elif i==2  or i==6:
                    matrizTablero.append([1, 2, 3, 3, 3, 3, 3, 2, 1]) 
                elif i==3  or i==5:
                    matrizTablero.append([1, 2, 3, 1, 1, 1, 3, 2, 1]) 
                else:
                    matrizTablero.append([1, 2, 3, 1, 2, 1, 3, 2, 1]) 

            return matrizTablero
         
        elif self.tipo == 'R':

            for i in range(filas):
                if i==0  or i==8:
                    matrizTablero.append([4, 4, 4, 4, 1, 4, 4, 4, 4])
                elif i==1  or i==7:
                    matrizTablero.append([4, 4, 4, 1, 2, 1, 4, 4, 4])      
                elif i==2  or i==6:
                    matrizTablero.append([4, 4, 1, 2, 3, 2, 1, 4, 4]) 
                elif i==3  or i==5:
                    matrizTablero.append([4, 1, 2, 3, 1, 3, 2, 1, 4]) 
                else:
                    matrizTablero.append([1, 2, 3, 1, 2, 1, 3, 2, 1]) 

            return matrizTablero
         
        elif self.tipo == 'D':
                                 
            for i in range(filas):
                matrizTablero.append([])
                for j in range(columnas):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            matrizTablero[i].append(1)        
                        elif j % 2 !=0:
                            matrizTablero[i].append(2)
                    elif i % 2 != 0:
                        if j % 2 == 0:
                            matrizTablero[i].append(2)        
                        elif j % 2 !=0:
                            matrizTablero[i].append(1)
            
            matrizTablero[5][6] = 1
            self.matrizTablero= matrizTablero

            return matrizTablero

    def getTablero(self): 
        return self.matrizTablero
    def setTablero(self,matrix): 
        self.matrizTablero = matrix
    def getColores(self):
        return self.colores
    def getTipo(self):
        return self.tipo

class Posicion:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def getFila(self) :
        return self.fila
    
    def setFila(self, fila) :
        self.fila = fila        

    def getColumna(self) :
        return self.columna        

    def setColumna(self, columna) :
        self.columna = columna

def empezar():
    menu1()

def menu1():    

   
    print "Elija tipo de tablero u otras opciones:"
    print "1. Facil"
    print "2. Intermedio"
    print "3. Dificil"
    print "4. Tablero fijo"
    print "5. Mejores puntuaciones"
    print "6. Borrar mejores puntuaciones"
    print "0. Salir"
    opcionMenu1 = int(input())


    while opcionMenu1<0 or opcionMenu1>6:
        print "Elija una opcion valida:"
        print "1. Facil"
        print "2. Intermedio"
        print "3. Dificil"
        print "4. Tablero fijo"
        print "5. Mejores puntuaciones"
        print "6. Borrar mejores puntuaciones"
        print "0. Salir"
        opcionMenu1 = int(input())

        tipoGenerico = 'G'

    if opcionMenu1==0:
        exit() 
    elif opcionMenu1==1:
        tab = Tablero(3,tipoGenerico)
        #print "Nivel Facil"        
    elif opcionMenu1==2:
        print "Nivel Intermedio"
    elif opcionMenu1==3:
        print "Nivel Dificil"
    elif opcionMenu1==4:
        print "Bienvenido a los tableros fijos"
    elif opcionMenu1==5:
        print "Bienvenido a Mejores Puntuaciones"
    elif opcionMenu1==6:
        print "Se han borrado las Mejores Puntuaciones"

objTablero = Tablero(3,'D')
matriz = objTablero.getTableroNuevo()

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print str(matriz[i][j]),

    print ''
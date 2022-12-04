# Desarrollar un algoritmo iterativo que permita calcular la bisección de una función f(x)

import math 

def f(x):


    return math.exp(x) - 2*x - 2    


def biseccion(a, b, tol):
    
        if f(a) * f(b) > 0:
            print("No hay raíz en el intervalo dado")
            return
    
        if f(a) == 0:
            print("La raíz es: ", a)
            return
    
        if f(b) == 0:
            print("La raíz es: ", b)
            return
    
        while True:
    
            c = (a + b) / 2
    
            if f(c) == 0:
                print("La raíz es: ", c)
                return
    
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
    
            if abs(f(c)) < tol:
                print("La raíz es: ", c)
                return


biseccion(0, 1, 0.0001)

#Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x)

import math

def f(x):

    return math.exp(x) - 2*x - 2


def secante(x0, x1, tol):
    
        while True:
    
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    
            if abs(f(x2)) < tol:
                print("La raíz es: ", x2)
                return
    
            x0 = x1
            x1 = x2
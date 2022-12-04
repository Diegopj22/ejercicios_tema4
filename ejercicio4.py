#Desarrolar un algoritmo númerico iterativo que permita calcular el método de la bisección de una función f(x).

import math

def f(x):
    return math.exp(-x) -x

def biseccion(a,b,tol):
    if f(a)*f(b)>0:
        print ("No hay raíz en el intervalo")
    else:
        while abs(b-a)>tol:
            c=(a+b)/2.0
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
        return c
        
print (biseccion(0,1,0.0001))


#Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x).

import math

def f(x):
    return math.exp(-x) -x

def secante(x0,x1,tol):
    while abs(x1-x0)>tol:
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0=x1
        x1=x2
    return x2

print (secante(0,1,0.0001))

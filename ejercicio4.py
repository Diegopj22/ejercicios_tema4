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


#Desarrollar un algoritmo numérico iterativo que permita calcular el método de Newton-Raphson de una función f(x).

import math

def f(x):
    return math.exp(-x) -x

def df(x):
    return -math.exp(-x) -1

def newton (x0,tol):
    while abs(f(x0))>tol:
        x0=x0-f(x0)/df(x0)
    return x0

print (newton(0,0.0001))


#Comparar los tres algoritmos anteriores para resolver la siguiente función: x3 + x +16 = 0, respecto de la cantidad de iteraciones necesarias por cada método para converger. ¿Cuánto es la diferencia en decimales entre las distintas soluciones?

import math

def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1

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

def secante(x0,x1,tol):
    while abs(x1-x0)>tol:
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0=x1
        x1=x2
    return x2

def newton (x0,tol):
    while abs(f(x0))>tol:
        x0=x0-f(x0)/df(x0)
    return x0

print ("Bisección: ",biseccion(-10,10,0.0001))
print ("Secante: ",secante(-10,10,0.0001))
print ("Newton-Raphson: ",newton(-10,0.0001))


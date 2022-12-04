class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

class nodoArbol(object):

    def __init__(self, info, nrr=None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr

def insertar_nodo(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    return raiz

def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)


#TABLA DE FRECUENCIAS
tabla = [['A', 0.09], ['B', 0.01], ['C', 0.03], ['D', 0.02], ['E', 0.12], ['G', 0.02], ['I', 0.05], ['L', 0.05], ['M', 0.02], ['N', 0.05], ['O', 0.06], ['P', 0.03], ['Q', 0.008], ['S', 0.03], ['T', 0.02], ['U', 0.03], ['V', 0.01], ['Espacio', 0.15], ['coma', 0.01]]
dic = {}

def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

for elemento in bosque:
    print(elemento.info, elemento.valor)
print()
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, cadena)


generar_tabla(bosque[0])

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod

def generar_diccionario(raiz, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
        else:
            cadena += '0'
            generar_diccionario(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_diccionario(raiz.der, cadena)


generar_diccionario(bosque[0])

print(dic)




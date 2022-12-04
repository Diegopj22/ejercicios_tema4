#Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos). Contemplar las siguientes consideraciones:
#cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre, en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva–;


class Vertice:
    """Representa un vértice de un grafo."""

    def __init__(self, info, tipo):
        """Crea un vértice con la información y el tipo."""
        self.info = info
        self.tipo = tipo
        self.adyacentes = Lista()
        self.visitado = False
        self.sig = None


class Adyacente:
    """Representa un adyacente de un vértice."""

    def __init__(self, destino, info):
        """Crea un adyacente con la información y el destino."""
        self.destino = destino
        self.info = info
        self.sig = None


class Lista:
    """Representa una lista enlazada."""

    def __init__(self):
        """Crea una lista enlazada vacía."""
        self.inicio = None
        self.tamanio = 0

    def insertar(self, destino, info):
        """Inserta un adyacente en la lista enlazada."""
        nuevo = Adyacente(destino, info)
        if(self.inicio is None):
            self.inicio = nuevo
        else:
            aux = self.inicio
            while(aux.sig is not None):
                aux = aux.sig
            aux.sig = nuevo
        self.tamanio += 1

    def barrido(self):
        """Realiza un barrido de la lista enlazada mostrando sus valores."""
        aux = self.inicio
        while(aux is not None):
            print(aux.destino, aux.info)
            aux = aux.sig


class Grafo:    
    """Representa un grafo no dirigido."""

    def __init__(self):
        """Crea un grafo no dirigido vacío."""
        self.inicio = None
        self.tamanio = 0

    def insertar_vertice(self, info, tipo):
        """Inserta un vértice en el grafo."""
        nuevo = Vertice(info, tipo)
        if(self.inicio is None):
            self.inicio = nuevo
        else:
            aux = self.inicio
            while(aux.sig is not None):
                aux = aux.sig
            aux.sig = nuevo
        self.tamanio += 1

    def insertar_arista(self, origen, destino, info):
        """Inserta una arista en el grafo."""
        aux = self.inicio
        while(aux is not None and aux.info != origen):
            aux = aux.sig
        if(aux is not None):
            aux.adyacentes.insertar(destino, info)
        aux = self.inicio
        while(aux is not None and aux.info != destino):
            aux = aux.sig
        if(aux is not None):
            aux.adyacentes.insertar(origen, info)

    def barrido(self):
        """Realiza un barrido del grafo mostrando sus valores."""
        aux = self.inicio
        while(aux is not None):
            print(aux.info, aux.tipo)
            aux.adyacentes.barrido()
            aux = aux.sig

    def barrido_anchura(self, vertice):
        """Realiza un barrido en anchura del grafo."""
        cola = Cola()
        aux = self.inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig
        aux = self.inicio
        while(aux is not None and aux.info != vertice):
            aux = aux.sig
        if(aux is not None):
            aux.visitado = True
            arribo_c(cola, aux)
            while(not cola_vacia(cola)):
                dato = atencion_c(cola)
                print(dato.info, dato.tipo)
                adyac = dato.adyacentes.inicio
                while(adyac is not None):
                    aux = self.inicio
                    while(aux is not None and aux.info != adyac.destino):
                        aux = aux.sig
                    if(aux is not None and not aux.visitado):
                        aux.visitado = True
                        arribo_c(cola, aux)
                    adyac = adyac.sig

#cada desvío puede tener múltiples puntos de entrada y salida


    def barrido_profundidad(self, vertice):
        """Realiza un barrido en profundidad del grafo."""
        pila = Pila()
        aux = self.inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig
        aux = self.inicio
        while(aux is not None and aux.info != vertice):
            aux = aux.sig
        if(aux is not None):
            aux.visitado = True
            apilar(pila, aux)
            while(not pila_vacia(pila)):
                dato = desapilar(pila)
                print(dato.info, dato.tipo)
                adyac = dato.adyacentes.inicio
                while(adyac is not None):
                    aux = self.inicio
                    while(aux is not None and aux.info != adyac.destino):
                        aux = aux.sig
                    if(aux is not None and not aux.visitado):
                        aux.visitado = True
                        apilar(pila, aux)
                    adyac = adyac.sig

#se deben cargar seis estaciones de trenes y doce cambios de agujas;


    def barrido_anchura2(self, vertice):
        """Realiza un barrido en anchura del grafo."""
        cola = Cola()
        aux = self.inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig
        aux = self.inicio
        while(aux is not None and aux.info != vertice):
            aux = aux.sig
        if(aux is not None):
            aux.visitado = True
            arribo_c(cola, aux)
            while(not cola_vacia(cola)):
                dato = atencion_c(cola)
                print(dato.info, dato.tipo)
                adyac = dato.adyacentes.inicio
                while(adyac is not None):
                    aux = self.inicio
                    while(aux is not None and aux.info != adyac.destino):
                        aux = aux.sig
                    if(aux is not None and not aux.visitado):
                        aux.visitado = True
                        arribo_c(cola, aux)
                    adyac = adyac.sig
















    

























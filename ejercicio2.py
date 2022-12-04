class HeapMax(object):

    def __init__(self):
        self.elementos = []
        self.tamanio = 0

    def vacio(self):
        return self.tamanio == 0

    def agregar(self, datos):
        self.elementos.append(datos)
        self.flotar(len(self.elementos)-1)
        self.tamanio += 1
    
    def flotar(self, indice):
        padre = (indice-1) // 2
        while(indice > 0 and self.elementos[indice] > self.elementos[padre]):
            self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
            indice = padre
            padre = (indice-1) // 2
    
    def quitar(self):
        self.elementos[0], self.elementos[self.tamanio-1] = self.elementos[self.tamanio-1], self.elementos[0]
        self.tamanio -= 1
        self.hundir()
        return self.elementos[self.tamanio]

    def hundir(self, indice=0):
        hijo_izq = indice * 2 + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if(self.elementos[hijo_der] > self.elementos[hijo_izq]):
                    aux = hijo_der
            
            if(self.elementos[indice] < self.elementos[aux]):
                self.elementos[indice], self.elementos[aux] = self.elementos[aux], self.elementos[indice]
                indice = aux
                hijo_izq = indice * 2 + 1
            else:
                control = False

    def heap_sort(self):
        for i in range(self.tamanio):
            self.quitar()
    
    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()

    def monticulizar(self, datos):
        self.elementos = datos
        self.tamanio = len(datos)
        for i in range(self.tamanio):
            self.flotar(i)
    
    def cambiar_prioridad(self, indice, prioridad):
        prioridad_anterio = self.elementos[indice][0] 
        self.elementos[indice][0] = prioridad
        if(prioridad_anterio < prioridad):
            self.flotar(indice)
        else:
            self.hundir(indice)


class HeapMin(object):
    
    def __init__(self):
        self.elementos = []
        self.tamanio = 0

    def busqueda(self, buscado):
        for index in range(self.tamanio):
            if(self.elementos[index][1][0] == buscado):
                return index
    

    def vacio(self):
        return self.tamanio == 0


    def agregar(self, datos):
        self.elementos.append(datos)
        self.flotar(len(self.elementos)-1)
        self.tamanio += 1
    
    def flotar(self, indice):
        padre = (indice-1) // 2
        while(indice > 0 and self.elementos[indice] < self.elementos[padre]):
            self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
            indice = padre
            padre = (indice-1) // 2
    
    def quitar(self):
        self.elementos[0], self.elementos[self.tamanio-1] = self.elementos[self.tamanio-1], self.elementos[0]
        self.tamanio -= 1
        self.hundir()
        dato = self.elementos[self.tamanio]
        self.elementos.pop()
        return dato

    def hundir(self, indice=0):
        hijo_izq = indice * 2 + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if(self.elementos[hijo_der] < self.elementos[hijo_izq]):
                    aux = hijo_der
            
            if(self.elementos[indice] > self.elementos[aux]):
                self.elementos[indice], self.elementos[aux] = self.elementos[aux], self.elementos[indice]
                indice = aux
                hijo_izq = indice * 2 + 1
            else:
                control = False

    def heap_sort(self):
        for i in range(self.tamanio):
            self.quitar()

    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()
    
    def monticulizar(self, datos):
        self.elementos = datos
        self.tamanio = len(datos)
        for i in range(self.tamanio):
            self.flotar(i)
    
    def cambiar_prioridad(self, indice, prioridad):
        prioridad_anterio = self.elementos[indice][0] 
        self.elementos[indice][0] = prioridad
        if(prioridad_anterio > prioridad):
            self.flotar(indice)
        else:
            self.hundir(indice)

#de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;


class Mision(object):

    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general

    def __str__(self):
        return f"tipo: {self.tipo}, planeta: {self.planeta}, general: {self.general}"


class Planeta(object):
    
        def __init__(self, nombre, x, y):
            self.nombre = nombre
            self.x = x
            self.y = y
    
        def __str__(self):
            return f"nombre: {self.nombre}, x: {self.x}, y: {self.y}"

class General(object):
        
        def __init__(self, nombre, x, y):
            self.nombre = nombre
            self.x = x
            self.y = y
        
        def __str__(self):
            return f"nombre: {self.nombre}, x: {self.x}, y: {self.y}"

# si la misión fue pedida por Palpatine o Darth Vader estas tendrán alta prioridad, sino su prioridad será baja;

def prioridad_mision(mision):
    if(mision.general.nombre == "Palpatine" or mision.general.nombre == "Darth Vader"):
        return 1
    else:
        return 0

#si la misión es de prioridad alta los recursos se asignarán manualmente independientemente de su tipo

def asignar_recursos(mision):
    if(prioridad_mision(mision) == 1):
        if(mision.tipo == "exploracion"):
            return 10
        elif(mision.tipo == "contencion"):
            return 5
        elif(mision.tipo == "ataque"):
            return 15
    else:
        return 0

#si la misión es de prioridad baja los recursos se asignarán de acuerdo a su tipo
#. exploración: 15 Scout Troopers y 2 speeder bike
# contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE,AT-DP, AT-ST) pueden ser repetidos,       
# ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT),

def asignar_recursos(mision):
    if(prioridad_mision(mision) == 1):
        if(mision.tipo == "exploracion"):
            return 10
        elif(mision.tipo == "contencion"):
            return 5
        elif(mision.tipo == "ataque"):
            return 15
    else:
        if(mision.tipo == "exploracion"):
            return 15
        elif(mision.tipo == "contencion"):
            return 30
        elif(mision.tipo == "ataque"):
            return 50

#realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, permitiendo agregar nuevos pedidos de misiones durante la atención;

def atender_misiones(misiones):
    misiones.monticulizar(misiones.elementos)
    misiones.heap_sort()
    while(misiones.tamanio > 0):
        mision = misiones.atencion()
        print(f"mision: {mision}, recursos: {asignar_recursos(mision)}")

#indicar la cantidad total de recursos asignados a las misiones.

def recursos_totales(misiones):
    misiones.monticulizar(misiones.elementos)
    misiones.heap_sort()
    total = 0
    while(misiones.tamanio > 0):
        mision = misiones.atencion()
        total += asignar_recursos(mision)
    return total


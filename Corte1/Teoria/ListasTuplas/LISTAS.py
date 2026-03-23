#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  #Creación de la lista de colores
#input()
print(my_lista)   #se imprime la lista
print(type(my_lista)) #Se imprime la clase de la variable, en este caso lista
print(my_lista[2])  #Se imprime el valor asignado a la posición 2 de la lista

print("my_lista size: ", len(my_lista))   #len entrega el tamaño de la lista, en este caso se usa para imprimir de que tamaño es la lista
print(my_lista[0:2]) #con [0:2] se imprimen los valores en las posiciones 0 y 2 sin incluir el límite superior
print(my_lista[:2]) #[:2] imprime lo mismo que el comando anterior, la diferencia es que en este caso si no se asigna un límite
                    #inferior se da por sentado que el límite inferior será 0

my_lista.append('Blanco')   #Agrega el elemento "blanco" al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro')   #Agrega el elemento "negro" en la posición 3 de la lista
print(my_lista)


my_lista.extend(['Marron', 'Gris'])   #Se genera una nueva lista de dos elementos y se concatena a la lista original
print(my_lista)

print(my_lista.index('Azul'))   #Con index y el nombre del elemento se obtiene la posición en la que este está 

my_lista.remove('Marron')  #con remove se busca el elemento "Marron" en la lista y lo elimina
print(my_lista)

my_lista.insert(8, 'Marron')  #se reinserta el elemento marrón a la lista en su posición original
print(my_lista)

print(my_lista.pop())  #pop elimina y retorna el último elemento de la lista y se imprime
size = len(my_lista)
print("size = ", size) #se imprime el tamaño actuañ de la lista
#print(my_lista.pop(size))

my_lista_3 = my_lista*3  # Crea una nueva lista repitiendo los elementos 3 veces
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_listaSort = my_lista.sort()  # Ordena la lista original alfabéticamente
print(my_listaSort)  # Imprime None porque sort() modifica la lista interna, no retorna valor

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  
print("Ordering my_NumList: ")
my_NumList.sort()  # Ordena los números de forma ascendente (1 a 10)
print(my_NumList) 
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)   #con reverse = True se invierte el orden del sort, organizando la lista de mayor a menor valor
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista) # Se usa el comando tuple() para convertir la lista de colores en una tupla
print()
print()
print("my_tuple: ", my_tupla) # Se imprime la tupla completa (ahora se ve con paréntesis en lugar de corchetes)

print(my_tupla[0])# Imprime el primer elemento de la tupla (posición 0)
print(my_tupla[2]) # Imprime el tercer elemento de la tupla (posición 2)

#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla) # El comando 'in' verifica si 'Rojo' existe dentro de la tupla
print(my_tupla.count('Rojo')) # count() cuenta cuántas veces se repite el elemento 'Rojo' en la tupla

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco') 
print(my_tupla_unitaria)

# Empaquetado de tupla: se crea la tupla asignando varios valores a una sola variable sin necesidad de paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre) # Imprime el valor guardado en la variable 'nombre' (Gaspar)
print(dia)    # Imprime el valor guardado en la variable 'dia' (5)
print(mes)    # Imprime el valor guardado en la variable 'mes' (8)
print(año)    # Imprime el valor guardado en la variable 'año' (1999)

# Se imprime un resumen combinando texto y las variables del desempaquetado
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla) # Se usa list() para que los datos de la tupla vuelvan a ser una lista y se puedan modificar
print(my_lista2)
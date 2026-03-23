###########################################################
# DICCIONARIOS PARTE 2: EXTRACCIÓN Y MANEJO DE DATOS
###########################################################

# 1. Acceso directo a valores
altura_edificios = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Ping An": 599}
# Accedemos usando la clave entre corchetes
print(f"La altura del Burj Khalifa es: {altura_edificios['Burj Khalifa']} metros")

# 2. Verificación de existencia (Evitar errores)
# Si buscamos algo que no existe como altura_edificios["BD Bacatá"], el programa falla.
# Por eso usamos un 'if' para validar antes:
buscar = "Landmark 81"
if buscar in altura_edificios:
    print(altura_edificios[buscar])
else:
    print(f"La clave '{buscar}' no se encuentra en el registro.")

# 3. Método .get() - La forma más segura de buscar
# .get() devuelve 'None' si no encuentra la clave, en lugar de romper el programa
print(f"Búsqueda segura (Shanghai): {altura_edificios.get('Shanghai Tower')}")
print(f"Búsqueda segura (Inexistente): {altura_edificios.get('BD Bacatá')}")

# 4. Eliminar datos con .pop()
# .pop() borra la clave y nos devuelve el valor que tenía
raffle = {223842: "Oso de Peluche", 872921: "Boletas Concierto", 412123: "Collar"}
premio_entregado = raffle.pop(872921, "No hay premio") 
print(f"Se entregó el premio: {premio_entregado}")
print(f"Rifa restante: {raffle}")

# 5. Obtener todas las llaves (.keys())
# Útil para saber qué nombres o IDs tenemos guardados
usuarios = {"teraCoder": 1000, "pythonGuy": 1829, "samJava": 1231}
print(f"Nombres de usuario registrados: {list(usuarios.keys())}")

# 6. Obtener todos los valores (.values())
# Útil para hacer cálculos matemáticos (como sumar totales)
ejercicios = {"funciones": 10, "sintaxis": 13, "bucles": 22}
total_ejercicios = 0
for cantidad in ejercicios.values():
    total_ejercicios += cantidad
print(f"Total de ejercicios realizados: {total_ejercicios}")

# 7. Obtener llaves y valores al tiempo (.items())
# Es la forma más usada para mostrar reportes o mensajes
marcas_valor = {"Apple": 184, "Google": 141, "Microsoft": 80}

print("\n--- REPORTE DE EMPRESAS ---")
for empresa, valor in marcas_valor.items():
    # 'empresa' toma la llave y 'valor' toma el número
    print(f"La empresa {empresa} tiene un valor de {valor} billones.")
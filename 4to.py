#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de
#los clientes de una empresa. El programa incorpora funciones crear el archivo con el listín si
#no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y
#eliminar el teléfono de un cliente. El listín debe estar guardado en el archivo de texto listin.txt
#donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada
#cliente en una línea distinta.





def creacion():
    nombre_archivo = "listin"
    numero = input("Inserte el número de teléfono que quiere crear: ")
    nombre = input("Inserte su nombre: ")
    try:
        # Abrir el archivo en modo escritura (agregar al final del archivo)
        with open(nombre_archivo, 'a') as archivo:
            # Escribir contenido en el archivo
            archivo.write(f"{nombre}:{numero}\n")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}' en modo escritura.")

# Llamar a la función para escribir en el archivo
creacion()


def borracion():
    nombre_archivo = "listin"
    numero = input("Inserte el número de teléfono que quiere borrar: ")
    try:
        # Leer el contenido del archivo
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        # Procesar y actualizar el contenido
        nuevo_contenido = []
        for linea in lineas:
            nombre, num = linea.strip().split(':')
            if num != numero:
                nuevo_contenido.append(linea.strip())
        
        # Escribir el contenido actualizado de vuelta al archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("\n".join(nuevo_contenido) + "\n")
            
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")

# Llamar a la función para borrar en el archivo
borracion()




def editacion():
    nombre_archivo = "listin"
    numero = int(input("inserte el numero de telefono que quiere borrar: "))
    try:
        # Leer el contenido del archivo
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        # Procesar y actualizar el contenido
        nuevo_contenido = []
        for linea in lineas:
            numeros = linea.split(", ")
            numeros_actualizados = []
            for num in numeros:
                if int(num) != numero:
                    numeros_actualizados.append(num)
            if numeros_actualizados:
                nuevo_contenido.append(", ".join(numeros_actualizados))
        
        # Escribir el contenido actualizado de vuelta al archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("\n".join(nuevo_contenido) + "\n")
            
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")

# Llamar a la función para escribir en el archivo
editacion()



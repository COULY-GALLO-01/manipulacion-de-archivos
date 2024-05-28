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
        with open(nombre_archivo, 'a') as archivo:
            
            archivo.write(f"{nombre}:{numero}\n")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}' en modo escritura.")

creacion()


def borracion():
    nombre_archivo = "listin"
    numero = input("Inserte el número de teléfono que quiere borrar: ")
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        nuevo_contenido = []
        for linea in lineas:
            nombre, num = linea.strip().split(':')
            if num != numero:
                nuevo_contenido.append(linea.strip())
        
        
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("\n".join(nuevo_contenido) + "\n")
            
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")


borracion()




def borracion():
    nombre_archivo = "listin"
    numero = input("Inserte el número de teléfono que quiere borrar: ")
    try:
       
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        
        nuevo_contenido = []
        for linea in lineas:
            nombre, num = linea.strip().split(':')
            if num != numero:
                nuevo_contenido.append(linea.strip())
        
       
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("\n".join(nuevo_contenido) + "\n")
            
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")


borracion()


def editacion():
    nombre_archivo = "listin"
    numero = input("Inserte el número de teléfono que quiere editar: ")
    nuevo_nombre = input("nombre: ")
    try:
        
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        
        nuevo_contenido = []
        for linea in lineas:
            nombre, num = linea.strip().split(':')
            if num == numero:
                nuevo_contenido.append(f"{nuevo_nombre}:{num}")
            else:
                nuevo_contenido.append(linea.strip())
        
       
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("\n".join(nuevo_contenido) + "\n")
            
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")


editacion()

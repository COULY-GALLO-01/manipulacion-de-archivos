# Solicitar al usuario que inserte un número
num = int(input("Inserte un número entre 1 y 10: "))

# Generar la lista de multiplicación
multiplicacion = [1*num, 2*num, 3*num, 4*num, 5*num, 6*num, 7*num, 8*num, 9*num, 10*num]

def multip():
    nombre_archivo = "tabla-n.txt"
    
    try:
        # Abrir el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            # Escribir contenido en el archivo
            
            archivo.write(", ".join(map(str, multiplicacion)) + "\n")
            
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}' en modo escritura.")

# Llamar a la función para escribir en el archivo
multip()

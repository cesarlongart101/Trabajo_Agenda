class Agenda:

    def obten_telefono(Self, fichero, persona):
        """
        El método obten_telefono recibe dos parámetos, el primero es el fichero en el cual se leen los datos.
        El segundo parámetro es persona que es el nombre ingresado por el usuario.
        Una vez recibidos ambos parámetros se abre el fichero en modo lectura y se itera en cada línea del mismo.
        Se ejecuta un condicional que valida si el parámetro persona se encuentra en la línea que está iterando, 
        si se valida se imprime la línea sino se encuentra se imprime un mensaje que dice que el registro no existe.
        """
        with open(fichero, "r") as archivo:
            for linea in archivo:
                if persona in linea:
                    print()
                    print("El número solicitado es: ")
                    print(linea)
                    return
            print()
            print("No existe en la agenda.")

    def inserta_telefono(Self, fichero, persona, telefono):
        """
        El método innserta_telefono recibe tres parámetros, el primero es el fichero, 
        el cual se abre en modo anexado para que los nuevos datos no sobrescriban los datos existentes.
        El segundo parámetro es persona que es el nombre ingresado por el usuario.
        El tercero es el teléfono que corresponde al número de teléfono ingresado por el usuario.
        Con los tres parámetros recibidos se ejecuta la función write al archivo (fichero) y se le indica agregar en una misma línea 
        separados por una coma y un espacio el parámetro persona y telefono.
        """
        with open(fichero, "a") as archivo:
            archivo.write(persona + ", " + telefono + "\n")

    def elimina_telefono(Self, fichero, persona):
        """
        El método elimina_telefono recibe dos parámetros, el primero es fichero, el cual se abre en modo lectura.
        El segundo es persona que es el nombre ingresado por el usuario que desea eliminar.
        Se ejecuta la funcion readlines() para leer todo el fichero y se guarda en una variable llamada líneas.
        Se define la variable encontrado con el valor False. 
        Se itera con la función enumerate así obtenemos la posición (número de línea) y el valor de la línea (nombre y teléfono).
        Se ejecuta el condicional verificando si el parámetro persona se encuentra en la línea iterada, si es así encontrado es True
        y se sale del ciclo for. Sino es econtrado se imprime en pantalla que no existe el dato en el archivo.
        A continuación, si encontrado es True se elimina la posición en la que se detuvo el ciclo for.
        Se abre nuevamente el fichero en modo escritura, se sobrescribe con el contenido de la variable lineas y se imprime
        en pantalla que se ha eliminado con éxito.
        """
        with open(fichero, "r") as archivo:
            lineas = archivo.readlines()

        encontrado = False
        for i, linea in enumerate(lineas):
            if persona in linea:
                encontrado = True
                break
        
        if encontrado:
            del lineas[i]
        
            with open(fichero, "w") as archivo:
                archivo.writelines(lineas)
            print("*** NOMBRE Y NÚMERO ELIMINADO CON ÉXITO ***")
        else:
            print("El nombre no existe en el archivo.")
        



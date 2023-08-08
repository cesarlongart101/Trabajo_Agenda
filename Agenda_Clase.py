class Agenda:

    def obten_telefono(Self, fichero, persona):
        with open(fichero, "r") as archivo:
            for linea in archivo:
                if persona in linea:
                    print(linea)
                    return
            print("No existe en la agenda.")

    def inserta_telefono(Self, fichero, persona, telefono):
        with open(fichero, "a") as archivo:
            archivo.write(persona + ", " + telefono + "\n")



    def elimina_telefono(Self, fichero, persona):
        with open(fichero, "r") as archivo:
            lineas = archivo.readlines()

        encontrado = False
        for i, linea in enumerate(lineas):
            if persona in linea:
                encontrado = True
                break
        
        if encontrado:
            del lineas[i]
        
            with open("agenda.txt", "w") as archivo:
                archivo.writelines(lineas)
            print("*** NOMBRE Y NÚMERO ELIMINADO CON ÉXITO ***")
        else:
            print("El nombre no existe en el archivo.")
        



class Agenda:


    def obten_telefono(fichero, persona):
        with open(fichero, "r") as archivo:
            for linea in archivo:
                print(linea)
        pass

    def inserta_telefono(fichero, persona, teléfono):
        nombre = "Juan"
        telefono = "123456789" 

        with open("contactos.txt", "a") as archivo:
            archivo.write(nombre + " , " + telefono + "\n")
        pass

    def elimina_telefono(fichero, persona):
        with open(fichero, "r+") as f:
            lineas = f.readlines()
            f.seek(0)
            for linea in lineas:
                if persona not in linea:
                    f.write(linea)
            f.truncate()
        pass


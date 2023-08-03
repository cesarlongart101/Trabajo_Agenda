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
            archivo.write(persona + "," + telefono + "\n")

    def elimina_telefono(Self, fichero, persona):
        with open(fichero, "r+") as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)
            for linea in lineas:
                if persona not in linea:
                    archivo.write(linea)
            archivo.truncate()


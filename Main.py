import Agenda_Clase
import Funciones_Utilitarias


fichero = "agenda.txt"
agenda = Agenda_Clase.Agenda()


def obten_telefono():
    
    while True:
        persona = input ("Nombre de la persona: ")
        if Funciones_Utilitarias.is_valid_name(persona):
            agenda.obten_telefono(fichero, persona)
            exit()
        

def inserta_telefono():
    pass

def elimina_telefono():
    pass

def salir_fun():
    print("*********************************************")  
    print("Has salido del programa.")
    print("*********************************************") 
    exit()


def default():
    print("Selecciona una opción valida dentro del menú")

cases = {
    "1": obten_telefono,
    "2": inserta_telefono,
    "3": elimina_telefono,
    "4": salir_fun
}

def menu():
    """Función definida para imprimir menú en pantalla y pedir una opción al usuario"""
    salir =True
    while salir:
        print()
        print("__________________")
        print("------ MENU ------")
        print("__________________")
        print()
        print("1. Obtener un teléfono. \n"
            "2. Insertar un teléfono. \n"
            "3. Eliminar un teléfono. \n"
            "4. Salir. \n")

        op = input("Seleccione una opción: ").strip()
        cases.get(op, default)()

menu ()
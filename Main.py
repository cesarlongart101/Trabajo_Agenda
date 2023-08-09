import Agenda_Clase
import Funciones_Utilitarias


fichero = "agenda.txt" 
agenda = Agenda_Clase.Agenda()


def obten_telefono():
    """
    Función que se usa para buscar un número telefónico dentro de la variable fichero. 
    Valida los caracteres ingresados por el usuario a través de la función utilitaria is_valid_name. 
    Llama al método obten_telefono de la clase Agenda validando si el nombre ingresado por el usuario existe.
    Una vez validado imprime en pantalla el número de teléfono, sino existe muestra un mensaje al usuario.
    """
    print("*** BUSCAR TELÉFONO ***")
    while True:
        persona = input ("Nombre de la persona: ").upper().strip()
        if Funciones_Utilitarias.is_valid_name(persona):
            agenda.obten_telefono(fichero, persona)
            break
        

def inserta_telefono():
    """
    Función que se usa para guardar en el archivo agenda.txt el nombre y número telefónico de un nuevo contacto ingresado por el usuario.
    Se le solicita al usuario ingresar nombre y número, se validan con las funciones utilitarias is_valid_name y is_valid_phone respectivamente.
    Una vez validados se llama al método inserta_telefono de la clase Agenda la cual procede a guardar las variables persona y número en el fichero.
    """
    print("*** GUARDAR EN AGENDA ***")
    while True:
        persona = input ("Nombre: ").upper().strip()
        if Funciones_Utilitarias.is_valid_name(persona):
            numero = input ("Número: ")
            if Funciones_Utilitarias.is_valid_phone(numero):
                agenda.inserta_telefono(fichero, persona, numero)
                print("*** NOMBRE Y NÚMERO GUARDADO CON ÉXITO ***")
                break
        

def elimina_telefono():
    """
    Función que se usa para eliminar un registro introducido por el usuario.
    Se solicita al usuario ingresar el nombre y se valida con la función utilitaria is_valid_name.
    Una vez validado se llama al método de la clase Ageda la cual procede a eliminar el registro indicado del fichero.
    """
    print("*** ELIMINAR EN AGENDA ***")
    while True:
        persona = input ("Nombre: ").upper().strip()
        if Funciones_Utilitarias.is_valid_name(persona):
            agenda.elimina_telefono(fichero, persona)
            break

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
def is_only_digits (num):
    """ Función utilitaria que valida que los dígitos ingresados sean números."""
    cont = 0
    for i in num:
        aux = ord(i)
        if aux not in range(48,58):
          print()
          print("Todos los caracteres deben ser numéricos")
          return False
        cont = cont + 1
        if cont == 9:
            return True
        

def is_valid_phone(phone):
    """ Función utilitaria que valida el número de teléfono y que llama a su vez a la función is_only_digits para validar que solo contenga números."""
    if len(phone) == 9:
        if phone[0] == "9" or phone[0] == "6":
            return is_only_digits(phone)
        else:
            print("El primer número debe ser 9 o 6.")
            return False
    else:
        print("El número debe tener 9 caracteres.")
        return False
    
def is_valid_name(name):
    """Función utilitaria que valida cadena de caracteres para nombre y apellido."""
    if len(name) > 1:
        cont = 0
        for i in name:
            aux = ord(i.lower())
            if (aux > 96 and aux < 123) or aux == 241 or aux == 32:
                cont = cont + 1
                if cont == len(name):
                    return True
            else:
                print("No se permiten números ni caracteres especiales en el nombre.")
                return False
    else:
        print("Al menos debe contener dos caracteres.")
        return False
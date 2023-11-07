# FUNCIÓN PARA VALIDAR LAS OPCIONES EN LOS MENÚS
def validateOptionInput(option, max, min=1):
    if option.isdigit():
        parsedOption = int(option)
        if (parsedOption > max or parsedOption < min):
            enter = input('La opción ingresada está fuera de rango')
        else:
            return True
    else:
        enter = input('La opción ingresada no es un número')

    return False


def inputModel(variable, notNull=True, isNumber=False, isRange=[], defaultValue=None):
    isValid = False
    while not isValid:
        data = input(variable.capitalize() + ': ')

        if not data and defaultValue:  # Para campos que tengan algo por defecto
            return defaultValue

        if isNumber:
            if data.isdigit():
                data = int(data)
            else:
                print('Tenés que ingresar un número en el campo de ' + variable)
                continue

        # Validaciones
        if notNull and not data:
            print('Tenés que completar el campo de ' + variable)
        elif not isRange and (isNumber and (data < isRange[0] or data > isRange[1])):
            print('El campo de ' + variable + ' tiene que estar entre ' +
                  str(isRange[0]) + ' y ' + str(isRange[1]))
        # AGREGAR VALIDACION DE RANGO DE STRING
        else:
            isValid = True
            return data

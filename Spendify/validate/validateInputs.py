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


# FUNCIÓN PARA CREAR Y VALIDAR INPUTS DEL MENÚ AÑADIR
def inputModel(variable, notNull = True, isNumber = False, isRange = []):
    data = input(variable.capitalize() + ': ')

    # Validaciones
    if notNull and len(data) == 0 :
        enter = input('Tenés que completar el campo de ' + variable)
    if isNumber and not data.isdigit() :
        enter = input('Tenés que ingresar un número en el campo de ' + variable)
    if len(isRange) and (data < isRange[0] or data > isRange[1]) :
        enter = input('El campo de ' + variable + 'tiene que estar entre ' + isRange[0] + 'y ' + isRange[1])

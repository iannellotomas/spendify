import os
from . import messages


# FUNCIÓN PARA VALIDAR LAS OPCIONES EN LOS MENÚS
def validateOptionInput(option="", maxValue=0, minValue=0, default_value=False):
    if option == "":
        if default_value is not False:
            return True
        else:
            messages.showError("La opción ingresada no puede estar vacía")
            return False
    elif isNumeric(option):
        parsed_option = int(option)
        if minValue <= parsed_option <= maxValue:
            return True
        else:
            messages.showError(f"Ingresá una opción entre {minValue+1} y {maxValue}")
            return False
    else:
        messages.showError("Tenés que ingresar un número")

    return False


def inputModel(
    variable,
    notNull=True,
    isNumber=False,
    isRange=[],
    defaultValue=None,
    clarification=False,
    clear=True,
):
    isValid = False
    while not isValid:
        if clear:
            clearConsole()
        if clarification:
            print("\n" + clarification)
        try:
            data = input("\n" + variable.capitalize() + ": ")
        except KeyboardInterrupt:
            os.system("cls")
            print("\n\t¡Vuelva pronto!")
            exit()

        data = data.strip()  # Sacar espacios al inicio y final de la cadena

        if not data and defaultValue:  # Para campos que tengan algo por defecto
            return defaultValue

        if isNumber:
            if isNumeric(data):
                data = int(data)
            else:
                messages.showError(
                    "Tenés que ingresar un número en el campo de " + variable
                )
                continue

        # Validaciones
        if notNull and not data and data != 0:
            messages.showError("Tenés que completar el campo de " + variable)
        elif isNumber and isRange and (data < isRange[0] or data > isRange[1]):
            messages.showError(
                "El campo de "
                + variable
                + " tiene que estar entre "
                + str(isRange[0])
                + " y "
                + str(isRange[1])
            )
        # AGREGAR VALIDACION DE RANGO DE STRING
        elif (
            not isNumber
            and isRange
            and (len(data) < isRange[0] or len(data) > isRange[1])
        ):
            messages.showError(
                "El campo de "
                + variable
                + " tiene que tener entre "
                + str(isRange[0])
                + " y "
                + str(isRange[1])
                + " caracteres"
            )
        else:
            isValid = True
            return data


# DefaultValue es por la posicion en la lista, se espera un INT
# ConvertValue es por si querés que se mantenga el valor en INT y no se pase al valor STR de la opción del array como "Efectivo" --> 1
def inputOptionModel(variable, array, defaultValue=None, convertValue=True, clear=True):
    isValidOption = False
    while not isValidOption:
        if clear:
            clearConsole()
        print(f"\n{variable.capitalize()}:")
        for i, option in enumerate(array):
            if i == defaultValue:
                print(f"{i + 1}- {option} (predeterminado)")
            else:
                print(f"{i + 1}- {option}")

        try:
            data = input("\nElegí una opción → ")
        except KeyboardInterrupt:
            os.system("cls")
            print("\n\t¡Vuelva pronto!")
            exit()

        data = data.replace(" ", "")  # Sacar todos los espacios

        if defaultValue != None and not data:  # Para campos que tengan algo por defecto
            if convertValue:
                return array[defaultValue]
            else:
                return defaultValue

        if isNumeric(data):
            data = int(data)
            if 1 <= data <= len(array):
                if convertValue:
                    return array[data - 1]
                else:
                    return data
            else:
                messages.showError(
                    f"Ingresá un número dentro del rango (1-{len(array)})"
                )
        else:
            messages.showError(
                f"Tenés que ingresar una de las opciones para {variable}"
            )


def clearConsole():
    os.system("cls")
    print(
        """
>> AÑADIR > GASTO
← VOLVER (V)
----------------------------------"""
    )


def isNumeric(str):
    if not str:
        return False
    for char in str:
        if not (char.isdigit() or (char == "0" and len(char) == 1)):
            return False
    return True

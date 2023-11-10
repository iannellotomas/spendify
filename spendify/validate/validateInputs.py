import os


# FUNCIÓN PARA VALIDAR LAS OPCIONES EN LOS MENÚS
def validateOptionInput(option="", maxValue=0, minValue=0, default_value=False):
    if option == "":
        if default_value is not False:
            return True
        else:
            showError("La opción ingresada no puede estar vacía")
            return False
    elif isNumeric(option):
        parsed_option = int(option)
        if minValue <= parsed_option <= maxValue:
            return True
        else:
            showError(
                f"Ingresá una opción entre {minValue+1} y {maxValue}")
            return False
    else:
        showError("Tenés que ingresar un número")

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
                showError(
                    "Tenés que ingresar un número en el campo de " + variable)
                continue

        # Validaciones
        if notNull and not data and data != 0:
            showError("Tenés que completar el campo de " + variable)
        elif isNumber and isRange and (data < isRange[0] or data > isRange[1]):
            showError(
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
            showError(
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
def inputOptionModel(variable, array, defaultValue=None, clear=True):
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
            return array[defaultValue]

        if isNumeric(data):
            data = int(data)
            if 1 <= data <= len(array):
                return array[data - 1]
            else:
                showError(
                    f"Ingresá un número dentro del rango (1-{len(array)})")
        else:
            showError(
                f"Tenés que ingresar una de las opciones para {variable}")


def clearConsole():
    os.system("cls")
    print(
        """
>> AÑADIR > GASTO
← VOLVER (V)
----------------------------------"""
    )


def showError(message=""):
    enter = input(
        f"""
(!) {message}\nENTER para aceptar """
    )


def isNumeric(str):
    if not str:
        return False
    for char in str:
        if not (char.isdigit() or (char == "0" and len(char) == 1)):
            return False
    return True

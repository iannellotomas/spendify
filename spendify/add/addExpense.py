import os
from datetime import datetime
from validate import validateInputs

# IMPORTAR DE LA BD
categoryList = [
    "Comida",
    "Salud",
    "Vivienda",
    "Entretenimiento",
]
currencyList = [
    "Peso argentino",
    "Dólar oficial",
    "Dólar blue",
]
payMethodList = [
    "Efectivo",
    "MercadoPago",
    "Tarjeta de Crédito",
    "Tarjeta de Débito",
    "Transferencia Bancaria",
    "Bitcoin",
]


def addExpense():
    os.system("cls")

    # Nombre del gasto
    name = validateInputs.inputModel("nombre del gasto")

    # Categoría del gasto
    category = validateInputs.inputOptionModel("categorías", categoryList)

    # Moneda de monto
    currency = validateInputs.inputOptionModel(
        "tipo de moneda", currencyList, defaultValue=0
    )
    # Monto del gasto
    amount = validateInputs.inputModel(
        "monto del gasto", isNumber=True, isRange=[1, 100000000]
    )
    # Método de pago
    payMethod = validateInputs.inputOptionModel(
        "método de pago", payMethodList, defaultValue=0
    )
    dues = {
        "total": 0,
        "paid": 0,
    }
    isValidDues = False
    first_iteration = True
    while first_iteration or not isValidDues:
        # Cuotas mensuales
        duesTotal = validateInputs.inputModel(
            "cuotas mensuales",
            isNumber=True,
            isRange=[-1, 400],
            defaultValue=1,
            clarification="0- Pago indefinido\n1- Sin cuotas (predeterminado)\nX- Número específico",
        )
        duesPaid = 0
        if duesTotal != 1:  # Para varias cuotas o pagos indefinidos
            duesPaid = (
                validateInputs.inputModel(  # Cuotas mensuales que hayan sido pagadas
                    "cuotas mensuales pagadas",
                    isNumber=True,
                    isRange=[0, 400],
                    defaultValue=0,
                    clear=False,
                )
            )

        if duesTotal == 0 or duesPaid <= duesTotal:
            dues["total"] = duesTotal
            dues["paid"] = duesPaid
            isValidDues = True
        else:
            showError(
                "Las cuotas que pagaste no pueden ser superiores a las cuotas totales"
            )

        first_iteration = False

    interests = 0
    if dues["total"] > 1:
        interests = validateInputs.inputModel(
            "porcentaje de intereses", isNumber=True, isRange=[1, 100]
        )

    date = {"day": 0, "month": 0, "year": 0}
    currentYear = datetime.now().year
    first_iteration = True
    while first_iteration or not isValidDate(
        date["day"], date["month"], date["year"], notFuture=True
    ):
        # Fecha del gasto
        date["day"] = validateInputs.inputModel(
            "día del gasto",
            notNull=False,
            isNumber=True,
            isRange=[1, 31],
            defaultValue="Hoy",
            clarification="ENTER- Hoy (predeterminado)",
        )
        if date["day"] != "Hoy":
            date["month"] = validateInputs.inputModel(
                "mes del gasto", isNumber=True, isRange=[1, 12], clear=False
            )
            date["year"] = validateInputs.inputModel(
                "año del gasto",
                isNumber=True,
                isRange=[1900, currentYear],
                clear=False,
            )
        else:
            currentDate = datetime.now()
            date = {
                "day": currentDate.day,
                "month": currentDate.month,
                "year": currentDate.year,
            }

        first_iteration = False

    expense = {
        "name": name,
        "category": category,
        "currency": currency,
        "amount": amount,
        "payMethod": payMethod,
        "dues": dues,
        "interests": interests,
        "date": date,
    }

    os.system("cls")
    print(
        """
>> AÑADIR > RESUMEN DE GASTO
← VOLVER (V)

//////////////////////////////////////
    """
    )

    showExpense(expense)
    decision = input(
        """
//////////////////////////////////////

¿Querés guardar el nuevo gasto?
- Si (S)
- No (N)

Elegí una opción → """
    ).upper()

    if decision == "S":
        notice(f"El gasto '{expense['name']}' se registró correctamente")
        return expense
    else:
        notice("El gasto no se guardó")
        return


def isValidDate(day, month, year, notFuture=False):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        enterDate = datetime(year, month, day)
        today = datetime.now()

        if notFuture and enterDate > today:
            showError("La fecha ingresada no puede ser futura")
            return False

        return True
    except ValueError:
        showError("La fecha ingresada no existe")
        return False


def showExpense(expense):
    translatedExpenses = (
        "Nombre del gasto",
        "Categoría",
        "Moneda",
        "Monto",
        "Método de pago",
        "Cuotas",
        "Intereses",
        "Fecha del gasto",
    )

    for i, (key, value) in enumerate(expense.items()):
        if key == "date":
            print(f"Fecha del gasto: {value['day']}/{value['month']}/{value['year']}")
        elif key == "dues":
            if value["total"] == 0:  # Para pagos indefinidos
                if value["paid"] == 0:
                    print(f"Cuotas: -")
                else:
                    print(f"Cuotas: {value['paid']} pagas")
            elif value["total"] > 1:  # Para pagos de varias cuotas
                print(f"Cuotas: {value['paid']} de {value['total']} pagas")
            else:  # Para pagos de una sola vez
                continue
        elif key == "interests":
            if expense["dues"]["total"] == 1:  # No mostrar intereses si no hay cuotas
                continue
            print(f"Intereses: {value}%")
        elif key == "amount":
            isoCode = ""
            match expense["currency"]:
                case "Peso argentino":
                    isoCode = "ARS"
                case "Dólar oficial":
                    isoCode = "USD"
                case "Dólar blue":
                    isoCode = "USDB"
            print(f"Monto: ${value} {isoCode}")
        elif key == "currency":  # No mostrar moneda por separado
            continue
        else:
            print(f"{translatedExpenses[i]}: {value}")


def showError(message=""):
    enter = input(
        f"""
(!) {message}\nENTER para aceptar """
    )


def notice(message=""):
    os.system("cls")

    enter = input(
        f"""
\t--- (i) ---\n{message}\n\nENTER para continuar """
    )

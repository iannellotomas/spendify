import os
from datetime import datetime
from historic import management
from utilities import messages, validateDate, validateInputs

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
        "tipo de moneda", currencyList, defaultValue=0, convertValue=False
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
        if duesTotal != 1:  # No mostrar para pagos de una sola vez
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
            messages.showError(
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
    while first_iteration or not validateDate.isValidDate(
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

    management.showExpense(expense)
    decision = input(
        """
//////////////////////////////////////

¿Querés guardar el nuevo gasto?
- Si (S)
- No (N)

Elegí una opción → """
    ).upper()

    if decision == "S":
        messages.notice(f"El gasto '{expense['name']}' se registró correctamente")
        # INSET INTO en las tablas de categoria y método de pago
        return expense
    else:
        messages.notice("El gasto no se guardó")
        return

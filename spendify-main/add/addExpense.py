import os
from datetime import datetime
from validate import validateInputs


def addExpense():
    # IMPORTAR DE LA BD
    categoryList = [
        "Comida",
        "Salud",
        "Vivienda",
        "Entretenimiento",
    ]

    os.system("cls")
    while True:
        print('''
>> AÑADIR > GASTO
← VOLVER (V)

        ''')

        name = validateInputs.inputModel("nombre del gasto")
        amount = validateInputs.inputModel(
            "monto del gasto", isNumber=True, isRange=[1, 100000000])

        dues = {
            "total": 0,
            "paid": 0,
        }
        isValidDues = False
        first_iteration = True
        while first_iteration and not isValidDues:
            duesTotal = validateInputs.inputModel(
                "cuotas mensuales", isNumber=True, isRange=[0, 400], defaultValue=1)
            duesPaid = 0
            if duesTotal != 1:  # En caso de ser pago único
                duesPaid = validateInputs.inputModel(
                    "cuotas mensuales pagadas", isNumber=True, isRange=[0, 400], defaultValue=0)

            if duesPaid <= duesTotal:
                dues["total"] = duesTotal
                dues["paid"] = duesPaid
                isValidDues = True

            first_iteration = False

        interests = 0
        if dues["total"] > 1:
            interests = validateInputs.inputModel(
                "porcentaje de intereses", isRange=[1, 100])

        date = {
            "day": 0,
            "month": 0,
            "year": 0
        }
        currentYear = datetime.now().year
        first_iteration = True
        while first_iteration or not isValidDate(date["day"], date["month"], date["year"]):
            date["day"] = validateInputs.inputModel(
                "día del gasto", isRange=[1, 31])
            date["month"] = validateInputs.inputModel(
                "mes del gasto", isRange=[1, 12])
            date["year"] = validateInputs.inputModel(
                "año del gasto", isRange=[1900, currentYear])

            first_iteration = False

        expense = {
            "name": name,
            "amount": amount,
            "dues": dues,
            "interests": interests,
            "date": date
        }

        os.system("cls")
        print('''
>> AÑADIR > RESUMEN DE GASTO
← VOLVER (V)

//////////////////////////////////////
        ''')

        showExpense(expense)
        decision = input('''
//////////////////////////////////////
¿Querés guardar el nuevo gasto?
- Si (S)
- No (N)

Elegí una opción → ''').upper()

        if decision == "S":
            return expense
        else:
            enter = input("El gasto no ha sido guardado")
            return


def isValidDate(day, month, year):
    fecha_str = f"{str(day)}/{str(month)}/{str(year)}"

    try:
        date = datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        enter = input("La fecha ingresada no existe")
        return False


def showExpense(expense):
    translatedExpenses = ("Nombre del gasto", "Monto", "Cuotas"
                          "Intereses", "Fecha del gasto")

    for i, (key, value) in enumerate(expense.items()):
        if key == "date":
            print(
                f"Fecha del gasto: {value['day']}/{value['month']}/{value['year']}")
        elif key == "dues":
            if value == 1:
                continue
            else:
                print(
                    f"Cuotas: {value['paid']} de {value['total']} pagas")
        elif key == "interests":
            print(
                f"Intereses: {value}%")
        else:
            print(f"{translatedExpenses[i]}: {value}")

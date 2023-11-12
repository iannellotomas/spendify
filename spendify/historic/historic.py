import os
from datetime import datetime
from utilities import validateInputs, validateDate
from . import management

expenses = [
    {
        "name": "Salida al cine",
        "category": "Entretenimiento",
        "currency": "Peso argentino",
        "amount": 1500,
        "payMethod": "MercadoPago",
        "dues": {"total": 1, "paid": 0},
        "interests": 0,
        "date": {"day": 10, "month": 11, "year": 2023},
    },
    {
        "name": "Suscripción de Netflix",
        "category": "Entretenimiento",
        "currency": "Dólar blue",
        "amount": 10,
        "payMethod": "Tarjeta de Crédito",
        "dues": {"total": 0, "paid": 12},
        "interests": 0,
        "date": {"day": 14, "month": 11, "year": 2017},
    },
    {
        "name": "Cena en restaurante",
        "category": "Comida",
        "currency": "Peso argentino",
        "amount": 5000,
        "payMethod": "Efectivo",
        "dues": {"total": 1, "paid": 0},
        "interests": 0,
        "date": {"day": 10, "month": 11, "year": 2023},
    },
]


def historic():
    while True:
        os.system("cls")
        print(
            """
>> HISTORIAL
← VOLVER (V)

//////////////////////////////////////
        """
        )

        if not expenses:
            enter = input(
                "\n\t____ (i) ____\nNo hay gastos guardados\nLos gastos que ingreses se mostrarán aquí "
            )
        else:
            sortedExpenses = sorted(
                expenses,
                key=lambda x: datetime(
                    x["date"]["year"], x["date"]["month"], x["date"]["day"]
                ),
                reverse=True,
            )

            currentCategory = None
            for i, value in enumerate(sortedExpenses):
                date_str = f"{value['date']['day']}/{value['date']['month']}/{value['date']['year']}"
                expenseDate = datetime(
                    value["date"]["year"], value["date"]["month"], value["date"]["day"]
                )
                category = validateDate.getDateLabel(expenseDate)

                if currentCategory != category:
                    if i > 0:
                        print("\n")
                    print(f"\n{category.upper()}\n---------------------------")
                    currentCategory = category

                currencyCode = ""
                if value["currency"] == "Peso argentino":
                    currencyCode = "ARS"
                elif value["currency"] == "Dólar oficial":
                    currencyCode = "USD"
                elif value["currency"] == "Dólar blue":
                    currencyCode = "USDB"

                print(
                    f"""{i+1}- {value['name']} ———— {value['category']} ———— ${value['amount']} {currencyCode}"""
                )

                if i == len(expenses) - 1:
                    print("\n")

            try:
                menuOption = input(
                    """
//////////////////////////////////////

Elegí una opción → """
                ).upper()

            except KeyboardInterrupt:
                os.system("cls")
                print("\n\t¡Vuelva pronto!")
                exit()

            if menuOption == "V":
                return

            if not validateInputs.validateOptionInput(menuOption, len(expenses), 0):
                continue
            else:
                menuOption = int(menuOption)
                os.system("cls")
                print(
                    """
>> HISTORIAL > DETALLE DEL GASTO
← VOLVER (V)

//////////////////////////////////////
                    """
                )
                management.showExpense(sortedExpenses[menuOption - 1])
                decision = input(
                    """
//////////////////////////////////////

Elegí una opción → """
                ).upper()

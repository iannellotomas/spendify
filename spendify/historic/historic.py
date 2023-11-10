import os
from datetime import datetime as dt, timedelta
from validate import validateOptionInput
from . import management
import locale

expenses = [
    {
        'name': 'Salida al cine',
        'category': 'Entretenimiento',
        'currency': 'Peso argentino',
        'amount': 1500,
        'payMethod': 'MercadoPago',
        'dues': {'total': 1, 'paid': 0},
        'interests': 0,
        'date': {'day': 10, 'month': 11, 'year': 2023}
    },
    {
        'name': 'Suscripción de Netflix',
        'category': 'Entretenimiento',
        'currency': 'Dólar blue',
        'amount': 10,
        'payMethod': 'Tarjeta de Crédito',
        'dues': {'total': 0, 'paid': 12},
        'interests': 0,
        'date': {'day': 14, 'month': 11, 'year': 2017}
    },
    {
        'name': 'Cena en restaurante',
        'category': 'Comida',
        'currency': 'Peso argentino',
        'amount': 5000,
        'payMethod': 'Efectivo',
        'dues': {'total': 1, 'paid': 0},
        'interests': 0,
        'date': {'day': 10, 'month': 11, 'year': 2023}
    }
]


def historic():
    while True:
        os.system("cls")
        print("""
>> HISTORIAL
← VOLVER (V)

//////////////////////////////////////
        """)

        if not expenses:
            enter = input(
                "\n\t____ (i) ____\nNo hay gastos guardados\nLos gastos que ingreses se mostrarán aquí ")
        else:
            sortedExpenses = sorted(expenses, key=lambda x: dt(
                x['date']['year'], x['date']['month'], x['date']['day']), reverse=True)

            currentCategory = None
            for i, value in enumerate(sortedExpenses):
                date_str = f"{value['date']['day']}/{value['date']['month']}/{value['date']['year']}"
                expenseDate = dt(
                    value['date']['year'], value['date']['month'], value['date']['day'])
                category = getDateCategory(expenseDate)

                if currentCategory != category:
                    if i > 0:
                        print("\n")
                    print(f"\n{category.upper()}\n---------------------------")
                    currentCategory = category

                currencyCode = ''
                if value['currency'] == 'Peso argentino':
                    currencyCode = 'ARS'
                elif value['currency'] == 'Dólar oficial':
                    currencyCode = 'USD'
                elif value['currency'] == 'Dólar blue':
                    currencyCode = 'USDB'

                print(
                    f"""{i+1}- {value['name']} ———— {value['category']} ———— ${value['amount']} {currencyCode}""")

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

            if not validateOptionInput(menuOption, len(expenses), 0):
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
                management.showExpense(sortedExpenses[menuOption-1])
                decision = input(
                    """
//////////////////////////////////////

Elegí una opción → """
                ).upper()


def getDateCategory(date):
    today = dt.now()
    yesterday = today - timedelta(days=1)
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)

    # Configuramos la configuración regional a español
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    if date.date() == today.date():
        return "Hoy"
    elif date.date() == yesterday.date():
        return "Ayer"
    elif date >= last_week:
        return "Esta semana"
    elif date >= last_month:
        return "Este mes"
    else:
        return date.strftime("%B %Y")


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

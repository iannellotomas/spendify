import os
from datetime import datetime
from utilities import validateInputs, validateDate
from queries import doQuery
from . import management


def historic(connectionObj):
    while True:
        os.system("cls")
        print(
            """
>> HISTORIAL
← VOLVER (V)

//////////////////////////////////////
        """
        )
        expenses = getExpenses(connectionObj)
        categoryList = getCategories(connectionObj)
        currencyList = getCurrencies(connectionObj)

        if not expenses:
            enter = input(
                "\n\t____ (i) ____\nNo hay gastos guardados\nLos gastos que ingreses se mostrarán aquí\n\nENTER para continuar"
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
                idCategory = value['category'] - 1
                currencyCode = currencyList[value["currency"]-1]["isocode"]

                print(
                    f"""{i+1}- {value['name']} ———— {categoryList[idCategory]['name']} ———— ${value['amount']:.2f} {currencyCode}"""
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
                print("\n\t¡Vuelva pronto!\n")
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
                management.showExpense(connectionObj, idExpense=menuOption)
                decision = input(
                    """
//////////////////////////////////////

Elegí una opción → """
                ).upper()


def getExpenses(connectionObj):
    sql = "SELECT id, nombre, id_categoria, id_moneda, monto, fecha FROM gastos"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    dataExpenses = []

    for expense in result:
        db_date = expense[5]
        formatted_date = db_date.strftime("%Y-%m-%d")

        # Extrae el día, mes y año de la fecha formateada
        year, month, day = map(int, formatted_date.split('-'))

        dataExpenses.append(
            {
                "id": expense[0],
                "name": expense[1],
                "category": expense[2],
                "currency": expense[3],
                "amount": expense[4],
                "date": {"day": day, "month": month, "year": year}
            }
        )
    return dataExpenses


def getCategories(connectionObj):
    sql = "SELECT id, nombre FROM categoria"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    dataCategories = []

    for category in result:
        dataCategories.append(
            {
                "id": category[0],
                "name": category[1]
            })

    return dataCategories


def getCurrencies(connectionObj):
    sql = "SELECT id, nombre, codigo FROM moneda"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    dataCurrency = []

    for category in result:
        dataCurrency.append(
            {
                "id": category[0],
                "name": category[1],
                "isocode": category[2]
            }
        )

    return dataCurrency

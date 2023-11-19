import os
from datetime import datetime
from historic import management
from utilities import messages, validateDate, validateInputs
from queries import doQuery


def addExpense(connectionObj):
    os.system("cls")

    # Nombre del gasto
    name = validateInputs.inputModel("nombre del gasto")

    # Categoría del gasto
    categoryList = getCategories(connectionObj)
    categoryNameList = list(map(getCategoryName, categoryList))
    categoryNameIndex = validateInputs.inputOptionModel(
        "categorías", categoryNameList, convertValue=False)

    categoryNameIndex = 1 if categoryNameIndex == 0 else categoryNameIndex

    chosenCategoryName = categoryNameList[categoryNameIndex-1]
    chosenCategoryID = getCategoryID(chosenCategoryName, categoryList)

    # Moneda de monto
    currencyList = getCurrencies(connectionObj)
    currencyNameList = list(map(getCurrencyName, currencyList))

    currencyNameIndex = validateInputs.inputOptionModel(
        "tipo de moneda", currencyNameList, defaultValue=0, convertValue=False
    )

    currencyNameIndex = 1 if currencyNameIndex == 0 else currencyNameIndex

    chosenCurrencyName = currencyNameList[currencyNameIndex-1]
    chosenCurrencyID = getCurrencyID(chosenCurrencyName, currencyList)

    # Monto del gasto
    amount = validateInputs.inputModel(
        "monto del gasto", isNumber=True, isRange=[1, 100000000]
    )

    # Método de pago

    payMethods = getPayMethods(connectionObj)
    payMethodsNameList = list(map(getPayMethodName, payMethods))

    payMethodNameIndex = validateInputs.inputOptionModel(
        "método de pago", payMethodsNameList, defaultValue=0, convertValue=False
    )

    payMethodNameIndex = 1 if payMethodNameIndex == 0 else payMethodNameIndex

    chosenPayMethodName = payMethodsNameList[payMethodNameIndex-1]
    chosenPayMethodID = getPayMethodID(chosenPayMethodName, payMethods)

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
        "id": getNextIdAvailable(connectionObj),
        "name": name,
        "category": chosenCategoryID,
        "currency": chosenCurrencyID,
        "amount": amount,
        "paymethod": chosenPayMethodID,
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

    management.showExpense(connectionObj, expense)
    decision = input(
        """
//////////////////////////////////////

¿Querés guardar el nuevo gasto?
- Si (S)
- No (N)

Elegí una opción → """
    ).upper()

    if decision == "S":
        saveExpense(connectionObj, expense)
        messages.notice(
            f"El gasto '{expense['name']}' se registró correctamente")

        return expense
    else:
        messages.notice("El gasto no se guardó")
        return


def saveExpense(connectionObj, expense):
    sql = """INSERT INTO gastos (
        id_usuario,
        nombre,
        id_categoria,
        id_moneda,
        monto,
        id_metodo,
        cantidad_cuotas,
        cantidad_cuotas_pagas,
        intereses,
        fecha
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (1, str(expense["name"]), int(expense["category"]), int(expense["currency"]), float(expense["amount"]), int(expense["payMethod"]), int(
        expense["dues"]["total"]), int(expense["dues"]["paid"]), int(expense["interests"]), str(f"{expense['date']['year']}-{expense['date']['month']}-{expense['date']['day']}"))

    doQuery(sql, 'INSERT', connectionObj, values=values)


def getNextIdAvailable(connectionObj):
    sql = "SELECT id FROM gastos"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)
    nextId = result[-1][0] + 1
    return nextId

def getCategories(connectionObj):
    sql = "SELECT id, nombre FROM categoria"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    categoriesData = []

    for category in result:
        categoriesData.append({"id": category[0], "nombre": category[1]})

    return categoriesData


def getCategoryName(category):
    return category["nombre"]


def getCurrencies(connectionObj):
    sql = "SELECT id, codigo, nombre FROM moneda"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    currenciesData = []

    for currency in result:
        currenciesData.append(
            {"id": currency[0], "codigo": currency[1], "nombre": currency[2]})

    return currenciesData


def getCategoryID(categoryName, categoryList):
    for category in categoryList:
        if (categoryName == category["nombre"]):
            return category["id"]

    return 0


def getCurrencyName(currency):
    return currency["nombre"]


def getCurrencyID(currencyName, currencyList):
    for currency in currencyList:
        if (currencyName == currency["nombre"]):
            return currency["id"]

    return 0


def getPayMethodID(payMethodName, payMethods):
    for payMethod in payMethods:
        if (payMethodName == payMethod["nombre"]):
            return payMethod["id"]

    return 0


def getPayMethods(connectionObj):
    sql = "SELECT id, nombre FROM metodos"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    payMethodsData = []

    for payMethod in result:
        payMethodsData.append({"id": payMethod[0], "nombre": payMethod[1]})

    return payMethodsData


def getPayMethodName(payMethods):
    return payMethods["nombre"]

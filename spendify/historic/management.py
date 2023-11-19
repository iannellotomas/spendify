from queries import doQuery


def showExpense(connectionObj, enterExpense = None, idExpense = None):
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
    expense = {}

    if not idExpense:
        expense = enterExpense
    else:
        expense = getExpense(idExpense, connectionObj)
    
    for i, (key, value) in enumerate(expense.items()):
        if key == "date":
            print(
                f"Fecha del gasto: {value['day']}/{value['month']}/{value['year']}")
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
        elif key == "category":
            print(
                f"{translatedExpenses[i-1]}: {getCategoryNameByID(expense['category'], connectionObj)}")
        elif key == "paymethod":
            print(
                f"{translatedExpenses[i-1]}: {getPayMethodNameByID(expense['paymethod'], connectionObj)}")
        elif key == "interests":
            if expense["dues"]["total"] == 1:  # No mostrar intereses si no hay cuotas
                continue
            print(f"Intereses: {value}%")
        elif key == "amount":
            print(
                f"Monto: ${value:.2f} {getCurrencyNameByID(expense['currency'], connectionObj)}")
        elif key == "currency" or key == "id":  # No mostrar moneda por separado
            continue
        else:
            print(f"{translatedExpenses[i-1]}: {value}")


def getCurrencyNameByID(currencyID, connectionObj):
    sql = f"SELECT codigo FROM moneda WHERE id = {currencyID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]


def getCategoryNameByID(categoryID, connectionObj):
    sql = f"SELECT nombre FROM categoria WHERE id = {categoryID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]


def getPayMethodNameByID(payMethodID, connectionObj):
    sql = f"SELECT nombre FROM metodos WHERE id = {payMethodID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]


def getExpense(idExpense, connectionObj):
    sql = f"SELECT id, nombre, id_categoria, id_moneda, monto, id_metodo, cantidad_cuotas, cantidad_cuotas_pagas, intereses, fecha FROM gastos ORDER BY fecha DESC"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    selectedExpense = result[idExpense-1]

    # Formatear fecha
    db_date = selectedExpense[9]
    formatted_date = db_date.strftime("%Y-%m-%d")

    # Extrae el día, mes y año de la fecha formateada
    year, month, day = map(int, formatted_date.split('-'))
    dataExpense = {
        "id": selectedExpense[0],
        "name": selectedExpense[1],
        "category": selectedExpense[2],
        "currency": selectedExpense[3],
        "amount": selectedExpense[4],
        "paymethod": selectedExpense[5],
        "dues": {"total": selectedExpense[6], "paid": selectedExpense[7]},
        "interests": selectedExpense[8],
        "date": {"day": day, "month": month, "year": year}
    }

    return dataExpense

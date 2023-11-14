import os
import datetime
from . import addExpense, addCategory, addBudget, addPayMethod
from utilities import validateInputs

# from queries import doQuery


def submenuAdd(connectionObj):
    while True:
        os.system("cls")
        print(
            """
>> AÑADIR
← VOLVER (V)
----------------------------------

1- INGRESAR UN GASTO
Registra los gastos de tu día a día

2- INGRESAR NUEVA CATEGORÍA
Te ayudará a identificar mejor tus gastos

3- ESTABLECER PRESUPUESTO
Te avisaremos cuando alcances los límites

4- AÑADIR UN MÉTODO DE PAGO
Define un tipo de pago, de forma anónima
        """
        )

        try:
            menuOption = input(
                """
----------------------------------
Elegí una opción → """
            )
        except KeyboardInterrupt:
            os.system("cls")
            print("\n\t¡Vuelva pronto!\n")
            exit()

        if menuOption.upper() != "V" and not (
            validateInputs.validateOptionInput(menuOption, 5)
        ):
            continue

        match menuOption:
            case "1":
                newExpense = addExpense.addExpense()
                break
                # newExpenseDate = newExpense["date"]
                # expenseDatetime = datetime.datetime(
                #     newExpenseDate["day"],
                #     newExpenseDate["month"],
                #     newExpenseDate["year"],
                # )
                # formattedDate = expenseDatetime.strftime("%Y-%m-%d")
                # sql = "INSERT INTO gastos (usuario, nombre, id_categoria, id_moneda, monto, id_metodo, cantidad_cuotas, cantidad_cuotas_pagas, intereses, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                # values = [
                #     1,
                #     newExpense["name"],
                #     newExpense["category"],
                #     newExpense["currency"],
                #     newExpense["amount"],
                #     newExpense["payMethod"],
                #     newExpense["dues"]["total"],
                #     newExpense["dues"]["paid"],
                #     formattedDate,
                # ]

                # values = [
                #     1,
                #     "Salida al cine",
                #     1,
                #     1,
                #     5000,
                #     1,
                #     3,
                #     2,
                #     "2023-11-10",
                # ]
                # doQuery(sql, "INSERT", values=values)
                # return
            case "2":
                newCategory = addCategory.addCategory(connectionObj)
                break
            case "3":
                newBudget = addBudget.addBudget(connectionObj)
                break
            case "4":
                newPayMethod = addPayMethod.addPayMethod()
                break
            case "v" | "V":
                print("Elegiste volver al menú principal")
                break

    return

import os
from . import setBudget, addExpense
from validate import validateOptionInput
from consultas import doQuery


def submenuAdd():
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
            print("\n\t¡Vuelva pronto!")
            exit()

        if menuOption.upper() != "V" and not (validateOptionInput(menuOption, 5)):
            continue

        match menuOption:
            case "1":
                newExpense = addExpense.addExpense()
                enter = input(str(newExpense))
                sql = "INSERT INTO gastos (usuario, nombre, id_categoría, id_moneda, monto, id_metodo_de_pago, cant_cuotas, cant_cuotas_pagas, intereses, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = [
                    newExpense['name'],
                    newExpense['category'],
                    newExpense['amount']
                ]
                doQuery(sql, 'INSERT', values=values)
                return
            case "2":
                print("Elegiste " + menuOption)
            case "3":
                setBudget.setBudget()
                pass
            case "4":
                print("Elegiste " + menuOption)
            case "v" | "V":
                print("Elegiste volver al menú principal")
                break

    return

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
    
    currencyIso = ("ARS", "USD", "USDB")

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
        elif key == "interests":
            if expense["dues"]["total"] == 1:  # No mostrar intereses si no hay cuotas
                continue
            print(f"Intereses: {value}%")
        elif key == "amount":
            print(f"Monto: ${value} {currencyIso[expense['currency']]}")
        elif key == "currency":  # No mostrar moneda por separado
            continue
        else:
            print(f"{translatedExpenses[i]}: {value}")

import os
from validate import validateInputs

budget = {"currency": "", "amount": 0}

currencyList = [
    "Peso argentino",
    "Dólar oficial",
    "Dólar blue",
]


def setBudget():
    os.system("cls")
    currency = validateInputs.inputOptionModel(
        "tipo de moneda", currencyList, defaultValue=0
    )
    amount = validateInputs.inputModel(
        "monto del presupuesto", isNumber=True, isRange=[1, 100000000]
    )

    budget["currency"] = currency
    budget["amount"] = int(amount)

    os.system("cls")
    print(
        """
>> AÑADIR > PRESUPUESTO FINAL
← VOLVER (V)

//////////////////////////////////////"""
    )

    translated = (
        "Moneda",
        "Monto",
    )

    print()

    for i, (key, value) in enumerate(budget.items()):
        print(translated[i] + ": " + str(value))

    enter = input(
        """
//////////////////////////////////////
\nENTER para volver al menú """
    )
    os.system("cls")
    return

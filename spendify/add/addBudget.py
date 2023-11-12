import os
from utilities import validateInputs

budget = {"currency": "", "amount": 0}

currencyList = [
    "Peso argentino",
    "Dólar oficial",
    "Dólar blue",
]


def addBudget():
    os.system("cls")
    currencyList = ["Peso argentino", "Dólar oficial", "Dólar blue"]

    currency_index = validateInputs.inputOptionModel(
        "tipo de moneda", currencyList, defaultValue=0, convertValue=False
    )

    amount = validateInputs.inputModel(
        "monto del presupuesto", isNumber=True, isRange=[1, 100000000]
    )

    os.system("cls")
    print(
        """
>> AÑADIR > PRESUPUESTO FINAL
← VOLVER (V)

//////////////////////////////////////"""
    )

    print(f"Moneda: {currencyList[currency_index]}")
    print(f"Monto: {int(amount)}")

    input(
        """
//////////////////////////////////////
\n\nENTER para volver al menú """
    )
    os.system("cls")

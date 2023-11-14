import os
from utilities import validateInputs
from queries import doQuery

budget = {"currency": "", "amount": 0}

currencyList = [
    "Peso argentino",
    "Dólar oficial",
    "Dólar blue",
]

currenciesCode = {
    "Peso argentino": "ARS",
    "Dólar oficial": "USD",
    "Dólar blue": "USDB"
}

def addBudget(connectionObj):
    os.system("cls")
    currencyList = ["Peso argentino", "Dólar oficial", "Dólar blue"]

    currency_index = validateInputs.inputOptionModel(
        "tipo de moneda", currencyList, defaultValue=0, convertValue=False
    )
    amount = validateInputs.inputModel(
        "monto del presupuesto", isNumber=True, isRange=[1, 100000000]
    )

    os.system("cls")
    print(currency_index)
    print(
        """
>> AÑADIR > PRESUPUESTO FINAL
← VOLVER (V)

//////////////////////////////////////"""
    )

    print(f"Moneda: {currencyList[currency_index-1]}")
    print(f"Monto: {int(amount)}")
    
    budget['amount'] = amount
    budget['currency'] = currenciesCode[currencyList[currency_index-1]]

    #addBudgetToDB(connectionObj, budget)
    updateUserBudget(connectionObj, budget)

    input(
        """
//////////////////////////////////////
\n\nENTER para volver al menú """
    )
    os.system("cls")

def addBudgetToDB(connectionObj, budget):
    print(budget)
    sql = "INSERT INTO usuarios (nombre, moneda, presupuesto, presupuesto_actual) VALUES (%s, %s, %s, %s)"
    values = ("test", budget['currency'], budget['amount'], budget['amount'])
    doQuery(sql, 'INSERT', connectionObj, values=values)

def updateUserBudget(connectionObj, budget):
    print(budget)
    sql = f"UPDATE usuarios SET nombre = '{'test'}', moneda = '{budget['currency']}', presupuesto = {budget['amount']}, presupuesto_actual = {budget['amount']} WHERE id = 1"
    doQuery(sql, 'UPDATE', connectionObj)




from add import submenuAdd
from search import submenuSearch
from utilities import validateInputs
from historic import historic, getBudgetReminder, getRecentExpenses
from bd import mysql_python
import os

while True:
    os.system("cls")
    connectionObj = mysql_python.makeConnection()
    mysql_python.checkConnnection(connectionObj)
    print(
        f"""
    \t ~~~~~~~~~~~~~~~~~~~
    \t       SPENDIFY 
    \t ~~~~~~~~~~~~~~~~~~~
{getBudgetReminder(connectionObj)}{getRecentExpenses(connectionObj)}
1- AÑADIR
Gastos, categorías, presupuesto y método de pago

2- BUSCAR
Encuentra gastos específicos

3- ANALIZAR
Mirá el seguimiento e informe de tus gastos

4- RESTABLECER
Borrá todo el historial de tus gastos

5- SALIR
No te preocupes ¡tus gastos quedan guardados!
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

    if not (validateInputs.validateOptionInput(menuOption, 5, 0, 0)):
        continue

    match menuOption:
        case "":
            historic(connectionObj)
        case "1":
            submenuAdd(connectionObj)
        case "2":
            submenuSearch()
        case "3":
            print("tres")
        case "4":
            print("cuatro")
        case "5":
            os.system("cls")
            print("\n\t¡Vuelva pronto!\n")
            exit()

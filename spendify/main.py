from add import submenuAdd
from search import submenuSearch
from validate import validateOptionInput
import os

while True:
    os.system("cls")
    print(
        """
\t ----------------------------------
\t             SPENDIFY 
\t ----------------------------------

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
        print("\n\t¡Vuelva pronto!")
        exit()

    if not (validateOptionInput(menuOption, 5)):
        continue

    match menuOption:
        case "1":
            submenuAdd()
        case "2":
            submenuSearch()
        case "3":
            print("tres")
        case "4":
            print("cuatro")
        case "5":
            os.system("cls")
            exit()

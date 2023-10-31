import os
# from budget import setBudget
from . import submenuAdd, budgetMenu, addExpense
#from validate import validateInputs
from validate import validateOptionInput
#import addExpense

def submenuAdd() :
    os.system("cls")
    while True:
        print('''
>> AÑADIR
← VOLVER (V)

1️⃣  INGRESAR UN GASTO 💸
Registra los gastos de tu día a día

2️⃣  INGRESAR NUEVA CATEGORÍA 💡
Te ayudará a identificar mejor tus gastos

3️⃣  ESTABLECER PRESUPUESTO 💰
Te avisaremos cuando alcances los límites

4️⃣  AÑADIR UN MÉTODO DE PAGO 💳
Define un tipo de pago, de forma anónima

        ''')

        menuOption = input('''
----------------------------------
Ingresá una opción → ''')

        if (not(validateOptionInput(menuOption, 5))):
            continue

        match menuOption:
            case '1':
                addExpense.addExpense()
            case '2':
                print('Elegiste ' + menuOption)
            case '3':
                budgetMenu()
                pass
            case '4':
                print('Elegiste ' + menuOption)
            case 'v', 'V':
                print('Elegiste volver al menú principal')
                return
                



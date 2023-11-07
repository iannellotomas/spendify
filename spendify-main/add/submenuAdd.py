import os
from . import setBudget, addExpense
from validate import validateInputs

def submenuAdd() :
    while True:
        os.system("cls")
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

        if (menuOption != 'V' and menuOption != 'v' and not(validateInputs.validateOptionInput(menuOption, 5))):
            continue

        match menuOption:
            case '1':
                addExpense.addExpense()
            case '2':
                print('Elegiste ' + menuOption)
            case '3':
                setBudget.setBudget()
                pass
            case '4':
                print('Elegiste ' + menuOption)
            case 'v':
                print('Elegiste volver al menú principal')
                break
            case 'V':
                print('Elegiste volver al menú principal')
                break
    
    return
                



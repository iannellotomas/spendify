from utilities import validateOptionInput
from . import searchByString
from . import searchByAmount
import os

def submenuSearch():
    while True:
        os.system("cls")
        print('''
>> BUSCAR
← VOLVER (V)

1️⃣  BUSCAR POR NOMBRE

2️⃣  BUSCAR POR CATEGORÍA

3️⃣  BUSCAR POR MÉTODO DE PAGO

4️⃣  BUSCAR POR MONTO
    
''')
        menuOption = input('''
----------------------------------
Ingresá una opción → ''')
        
        if (menuOption != 'V' and menuOption != 'v' and not(validateOptionInput(menuOption, 4))):
            continue

        match menuOption:
            case '1' | '2' | '3':
                searchByString.submenuSearchByString(menuOption)
                break
            case '4':
                searchByAmount.submenuSearchByAmount()
                break
            case 'v':
                print('Elegiste volver al menú principal')
                break
            case 'V':
                print('Elegiste volver al menú principal')
                break
    
    return
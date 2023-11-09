import os
from validate import validateOptionInput

def submenuSearchByAmount():
    while True:
        os.system("cls")
        print('''
BÚSQUEDA POR MONTO

1️⃣ MONTOS SUPERIORES
Te ayudará a buscar montos superiores
              
2️⃣ MONTOS INFERIORES
Te ayudará a buscar montos inferiores
              
3️⃣ MONTOS IGUALES
Te ayudará a buscar montos iguales
      
''')
        
        menuOption = input('''
----------------------------------
Ingresá una opción → ''')
        
        if (menuOption != 'V' and menuOption != 'v' and not(validateOptionInput(menuOption, 3))):
            continue
        
        match menuOption:
            case '1':
                searchByAmount('+')
            case '2':
                searchByAmount('-')
            case '3':
                searchByAmount('=')

        enter = input("\nPresione ENTER para volver al menú")
        break

    return

def searchByAmount(indicator):
    amount = amountInput()

    match indicator:
        case '+':
            print(f'Mayor a {amount}')
        case '-':
            print(f'Menor a {amount}')
        case '=':
            print(f'Igual a {amount}')
    
    return

def amountInput():
    amount = 0
    while True:
        os.system("cls")
        amount = input('''
Ingrese el monto: 
''')
        break
    
    return amount
        
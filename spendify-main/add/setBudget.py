import os
from validate import validateInputs

budget = {
    "currency": "",
    "amount": 0
}

def setBudget():
    while True:
        os.system('cls')
        printSubmenuCurrency()
        option = input('Selecciona las opciones de moneda disponibles (1-3): ')
        if(not(validateInputs.validateOptionInput(option, 3))):
            continue
        
        match option:
            case '1':
                budget['currency'] = 'ARS'
            case '2':
                budget['currency'] = 'USD' 
            case '3':
                budget['currency'] = 'USDB'
            case '':
                budget['currency'] = 'ARS'
        break
        
    while True:
        os.system('cls')
        min,max = printSubmenuAmountRange(budget['currency'])
        amount = input("Ingrese el monto del presupuesto: ")
        if(not(validateInputs.validateOptionInput(amount, max, min))):
            continue
        
        budget['amount'] = int(amount)
        break
    
    print("\n> PRESUPUESTO FINAL")
    print(budget['amount'], budget['currency'])
    enter = input('\nPresione enter para volver al menú')
    os.system("cls")
    return

def printSubmenuAmountRange(currency):
    min = 0
    max = 0

    match currency:
        case 'ARS':
            print(f'Rango {currency} 10000-100.000.000')
            max = 100000000
            min = 10000
        case "USD":
            print(f'Rango {currency} 100-1.000.000')
            max = 1000000
            min = 100
        case "USDB":
            print(f'Rango {currency} 100-1.000.000')
            max = 1000000
            min = 100
        
    return (min, max)
    
        
def printSubmenuCurrency():
    print('''
1) Pesos Argentinos
2) Dólar Oficial
3) Dólar Blue
    ''')

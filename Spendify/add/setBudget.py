import os
from validate.validateInputs import validateOptionInput

budget = {
    "currency": "",
    "amount": 0
}

def setBudget():
    while True:
        os.system('cls')
        printSubmenuCurrency()
        option = input('Selecciona las opciones de moneda disponibles (1-3): ')
        if(not(validateOptionInput(option, 3))):
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
        if(not(validateOptionInput(amount, max, min))):
            continue
        
        budget['amount'] = int(amount)
        break
    
    print("PRESUPUESTO FINAL")
    print(budget['amount'], budget['currency'])

def printSubmenuAmountRange(currency):
    match currency:
        case 'ARS':
            print(f'{currency} 10000-100.000.000')
            return 10000, 100000000
        case 'USD', 'USDB':
            print(f'{currency} 100-1.000.000')
            return 100, 1000000
    
        
def printSubmenuCurrency():
    print('''
1) Pesos Argentinos
2) Dólar Oficial
3) Dólar Blue
    ''')

import os
from utilities import validateInputs
from . import resetDB

def submenuResetDB(connectionObj, user):
    while True:
        os.system("cls")
        print("""
← VOLVER (V)
----------------------------------
Desea restablecer el historial de gastos?

1- Si
2- No 
""")
        try:
            menuOption = input('''----------------------------------
Ingresá una opción → ''')
        except KeyboardInterrupt:
            os.system("cls")
            print("\n\t¡Vuelva pronto!\n")
            exit()
        
        if (menuOption != 'V' and menuOption != 'v' and not(validateInputs.validateOptionInput(menuOption, 2))):
            continue
    
        match menuOption:
            case '1':
                resetDB.resetDB(connectionObj, user)
                break
            case '2':
                print("Restablecimiento cancelado")
                break
            case 'v':
                print('Elegiste volver al menú principal')
                break
            case 'V':
                print('Elegiste volver al menú principal')
                break
    
    return

    

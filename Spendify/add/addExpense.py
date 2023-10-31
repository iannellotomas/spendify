import os
from datetime import datetime

def addExpense() :
    # IMPORTAR DE LA BD
    categoryList = [
        "Comida"
        "Salud"
        "Vivienda"
        "Entretenimiento"
    ]
    
    os.system("cls")
    while True:
        print('''
>> AÑADIR > GASTO
← VOLVER (V)


----------------------------------
        ''')

        name = inputModel("nombre del gasto")
        amount = inputModel("monto del gasto", isNumber=True, isRange=[1, 100000000])
        dues = inputModel("cuotas mensuales", isRange=[0, 400])
        if dues == 1:
            interests = inputModel("porcentaje de intereses", isRange=[1, 100])
        
        date = {
            "day": 0,
            "month": 0,
            "year": 0
        }
        currentYear = datetime.now().year
        
        while not isValidDate(date[day], date[month], date[year]):
            date[day] = inputModel("dia del gasto", isRange=[1, 31])
            date[month] = inputModel("mes del gasto", isRange=[1, 12])
            date[year] = inputModel("año del gasto", isRange=[1900, currentYear])

        gasto = [
            name,
            amount,
            interests,
            date
        ]

        enter = input("El gasto es: " + gasto)
    

    
                
def isValidDate(day, month, year):
    fecha_str = f"{day}/{month}/{year}"
    
    try:
        date = datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        enter = input("La fecha ingresada no existe")
        return False
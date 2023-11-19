import os
from utilities import messages, validateInputs
from queries import doQuery

def addPayMethod(connectionObj):
    while True:
        os.system("cls")
        print(
            """
>> AÑADIR > MÉTODO DE PAGO
← VOLVER (V)
----------------------------------"""
        )

        payMethods = getPayMethods(connectionObj)
        payMethodsNameList = list(map(getPayMethodName, payMethods))

        payMethod = validateInputs.inputModel(
            "método de pago", isRange=[1, 30], clear=False
        )
        #habría que añadir una condicion donde se eliminen espacios por si el usuario ingresa el metodo de pago sin espacios
        if not any(payMethod.upper() == item.upper() for item in payMethodsNameList):
            savePayMethod(connectionObj, payMethod)
            
            messages.notice(
                f"El método de pago '{payMethod}' se registró correctamente"
            )

            break
        else:
            messages.showError("Existe un método de pago con el mismo nombre")

def getPayMethods(connectionObj):
    sql = "SELECT id, nombre FROM metodos"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    payMethodsData = []

    for payMethod in result:
        payMethodsData.append({"id": payMethod[0], "nombre": payMethod[1]})
    
    return payMethodsData

def getPayMethodName(payMethods):
    return payMethods["nombre"]

def savePayMethod(connectionObj, payMethod):
    values = (payMethod, )
    sql = "INSERT INTO metodos (nombre) VALUES (%s)"
    doQuery(sql, 'INSERT', connectionObj, values=values)
import os
from utilities import messages, validateInputs
from queries import doQuery

def addCategory(connectionObj):
    while True:
        os.system("cls")

        categoryList = getCategoriesNameFromDB(connectionObj)
        
        print(
            """
>> AÑADIR > CATEGORÍA
← VOLVER (V)
----------------------------------"""
        )

        category = validateInputs.inputModel("categoría", isRange=[1, 30], clear=False)

        if not any(category.upper() == item.upper() for item in categoryList):
            saveCategory(connectionObj, category)
            messages.notice(f"La categoría '{category}' se registró correctamente")
            return category
        else:
            messages.showError("Existe una categoría con el mismo nombre")


def getCategoriesNameFromDB(connectionObj):
    sql = "SELECT nombre FROM categoria"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    categories = []

    for category in result:
        categories.append(category[0])

    return categories

def saveCategory(connectionObj, category):
    values = (category, )
    sql = "INSERT INTO categoria (nombre) VALUES (%s)"
    doQuery(sql, 'INSERT', connectionObj, values=values)
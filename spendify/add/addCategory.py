import os
from utilities import messages, validateInputs
from queries import doQuery

# IMPORTAR DE LA BD
# categoryList = [
#     "Comida",
#     "Salud",
#     "Vivienda",
#     "Entretenimiento",
# ]


def addCategory(connectionObj):
    while True:
        os.system("cls")

        categoryList = getCategoriesFromDB(connectionObj)
        print(categoryList)
        print(
            """
>> AÑADIR > CATEGORÍA
← VOLVER (V)
----------------------------------"""
        )

        category = validateInputs.inputModel("categoría", isRange=[1, 30], clear=False)

        if not any(category.upper() == item.upper() for item in categoryList):
            messages.notice(f"La categoría '{category}' se registró correctamente")
            return category
        else:
            messages.showError("Existe una categoría con el mismo nombre")


def getCategoriesFromDB(connectionObj):
    sql = "SELECT nombre FROM categoria"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)
    return result
import os
from utilities import messages, validateInputs

# IMPORTAR DE LA BD
categoryList = [
    "Comida",
    "Salud",
    "Vivienda",
    "Entretenimiento",
]


def addCategory():
    while True:
        os.system("cls")
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

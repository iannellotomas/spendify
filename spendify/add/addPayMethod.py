import os
from utilities import messages, validateInputs

# IMPORTAR DE LA BD
payMethodList = [
    "Efectivo",
    "MercadoPago",
    "Tarjeta de Crédito",
    "Tarjeta de Débito",
    "Transferencia Bancaria",
    "Bitcoin",
]


def addPayMethod():
    while True:
        os.system("cls")
        print(
            """
>> AÑADIR > MÉTODO DE PAGO
← VOLVER (V)
----------------------------------"""
        )

        payMethod = validateInputs.inputModel(
            "método de pago", isRange=[1, 30], clear=False
        )

        if not any(payMethod.upper() == item.upper() for item in payMethodList):
            messages.notice(
                f"El método de pago '{payMethod}' se registró correctamente"
            )
            return payMethod
        else:
            messages.showError("Existe un método de pago con el mismo nombre")

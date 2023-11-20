from datetime import datetime
from queries import doQuery
from historic import management

# expenses = [
#     {
#         "name": "Salida al cine",
#         "category": "Entretenimiento",
#         "currency": 1,
#         "amount": 1500,
#         "payMethod": "MercadoPago",
#         "dues": {"total": 1, "paid": 0},
#         "interests": 0,
#         "date": {"day": 10, "month": 11, "year": 2023},
#     },
#     {
#         "name": "Suscripción de Netflix",
#         "category": "Entretenimiento",
#         "currency": 3,
#         "amount": 10,
#         "payMethod": "Tarjeta de Crédito",
#         "dues": {"total": 0, "paid": 12},
#         "interests": 0,
#         "date": {"day": 14, "month": 11, "year": 2017},
#     },
#     {
#         "name": "Cena en restaurante",
#         "category": "Comida",
#         "currency": 1,
#         "amount": 5000,
#         "payMethod": "Efectivo",
#         "dues": {"total": 1, "paid": 0},
#         "interests": 0,
#         "date": {"day": 10, "month": 11, "year": 2023},
#     },
# ]


def getRecentExpenses(connectionObj):
    header = "GASTOS RECIENTES\n------------------------------------"
    footer = "\n\nENTER → VER TODOS MIS GASTOS\n-----------------------------------\n"
    currencyIso = ("ARS", "USD", "USDB")
    
    sql = "SELECT nombre, id_categoria, monto, id_moneda, fecha FROM gastos ORDER BY fecha DESC LIMIT 3"
    expenses = doQuery(sql, "SELECT", connectionObj, doReturn=True)

    if len(expenses) == 0:
        return ""

    processedExpenses = []

    for expense in expenses:
        processedExpenses.append({
            'name': expense[0],
            'category': expense[1],
            'amount': expense[2],
            'currency': expense[3],
            'date': expense[4]
        })
    
    # Utiliza una función de clave para ordenar por fecha
    #recentExpenses = sorted(processedExpenses, key=lambda x: datetime(**x["date"]), reverse=True)[:3]

    expenseLines = [
        f"{expense['name']} ———————— {management.getCategoryNameByID(expense['category'], connectionObj)} ———————— ${expense['amount']} {currencyIso[expense['currency']-1]} "
        for expense in processedExpenses
    ]

    message = f"{header}\n"
    message += "\n".join(expenseLines)
    message += footer

    return message
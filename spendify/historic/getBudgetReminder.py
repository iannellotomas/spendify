import os
from queries import doQuery

def getBudgetReminder(connectionObj):

    budgetsFromDB = getBudgetsFromDB(connectionObj, 1)

    definedBudget = budgetsFromDB[0][0]
    reachedBudget = budgetsFromDB[0][1]
    currencyBudget = budgetsFromDB[0][2]
    
    percentReached = (
        min((reachedBudget / definedBudget) * 100, 100) if definedBudget != 0 else 0
    )

    message = ""

    if percentReached >= 75:
        message += """
----------------------------------------------
   (!) LÍMITE DE PRESUPUESTO ALCANZADO (!)
----------------------------------------------
    """

    message += f"""
PRESUPUESTO: ${reachedBudget} / ${definedBudget} {currencyBudget} 
{showPercentage(percentReached)}\n
    """

    #connectionObj.close()

    return message


def showPercentage(percentage):
    barLength = 20
    numBlocks = int(percentage / 5)
    numSpaces = barLength - numBlocks

    bar = "=" * numBlocks + " " * numSpaces
    return f"[{bar}] {percentage:.2f}%"


def getBudgetsFromDB(connectionObj, userID):
    sql = f"SELECT presupuesto, presupuesto_actual, moneda FROM usuarios WHERE id = {userID}"

    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    #print(result)

    return result
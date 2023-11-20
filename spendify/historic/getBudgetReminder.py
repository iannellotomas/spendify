import os
from queries import doQuery
from add import addBudget

def getBudgetReminder(connectionObj):

    budgetsFromDB = getBudgetsFromDB(connectionObj, 1)

    addBudget.updateUserBudget(connectionObj, {"amount": budgetsFromDB[0][0], "currency": budgetsFromDB[0][2]})
    os.system("cls")

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
PRESUPUESTO: ${reachedBudget} / ${definedBudget} {getCurrencyByID(currencyBudget, connectionObj)} 
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

    return result

def getCurrencyByID(currencyID, connectionObj):
    sql = f"SELECT codigo FROM moneda WHERE id = {currencyID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]
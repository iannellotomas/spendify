import os


def getBudgetReminder():
    currencyIso = ("ARS", "USD", "USDB")
    currencyBudget = 2

    definedBudget = 2000
    reachedBudget = 870
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
PRESUPUESTO: ${reachedBudget} / ${definedBudget} {currencyIso[currencyBudget-1]} 
{showPercentage(percentReached)}\n
    """

    return message


def showPercentage(percentage):
    barLength = 20
    numBlocks = int(percentage / 5)
    numSpaces = barLength - numBlocks

    bar = "=" * numBlocks + " " * numSpaces
    return f"[{bar}] {percentage:.2f}%"

from utilities import messages, validateDate, validateInputs
from datetime import datetime
from add import addExpense

def editName():
  name = validateInputs.inputModel("nombre del gasto")
  return name

def editCategory(connectionObj):
  categoryList = addExpense.getCategories(connectionObj)
  categoryNameList = list(map(addExpense.getCategoryName, categoryList))
  categoryNameIndex = validateInputs.inputOptionModel("categorías", categoryNameList, convertValue=False)
  categoryNameIndex = 1 if categoryNameIndex == 0 else categoryNameIndex
  chosenCategoryName = categoryNameList[categoryNameIndex-1]
  chosenCategoryID = addExpense.getCategoryID(chosenCategoryName, categoryList)

  return chosenCategoryID

def editCurrency(connectionObj):
  currencyList = addExpense.getCurrencies(connectionObj)
  currencyNameList = list(map(addExpense.getCurrencyName, currencyList))

  currencyNameIndex = validateInputs.inputOptionModel("tipo de moneda", currencyNameList, defaultValue=0, convertValue=False)

  currencyNameIndex = 1 if currencyNameIndex == 0 else currencyNameIndex

  chosenCurrencyName = currencyNameList[currencyNameIndex-1]
  chosenCurrencyID = addExpense.getCurrencyID(chosenCurrencyName, currencyList)
  
  return chosenCurrencyID

def editAmount():
  amount = validateInputs.inputModel("monto del gasto", isNumber=True, isRange=[1, 100000000])
  
  return amount

def editPayMethod(connectionObj):
  payMethods = addExpense.getPayMethods(connectionObj)
  payMethodsNameList = list(map(addExpense.getPayMethodName, payMethods))

  payMethodNameIndex = validateInputs.inputOptionModel("método de pago", payMethodsNameList, defaultValue=0, convertValue=False)

  payMethodNameIndex = 1 if payMethodNameIndex == 0 else payMethodNameIndex

  chosenPayMethodName = payMethodsNameList[payMethodNameIndex-1]
  chosenPayMethodID = addExpense.getPayMethodID(chosenPayMethodName, payMethods)

  return chosenPayMethodID

def editDues():
  dues = {
    "total": 0,
    "paid": 0,
  }
  isValidDues = False
  first_iteration = True
  while first_iteration or not isValidDues:
    # Cuotas mensuales
    duesTotal = validateInputs.inputModel(
      "cuotas mensuales",
      isNumber=True,
      isRange=[-1, 400],
      defaultValue=1,
      clarification="0- Pago indefinido\n1- Sin cuotas (predeterminado)\nX- Número específico",
    )
    
    duesPaid = 0
        
    if duesTotal != 1:  # No mostrar para pagos de una sola vez
      duesPaid = (
        validateInputs.inputModel(  # Cuotas mensuales que hayan sido pagadas
          "cuotas mensuales pagadas",
          isNumber=True,
          isRange=[0, 400],
          defaultValue=0,
          clear=False,
        )
      )

    if duesTotal == 0 or duesPaid <= duesTotal:
      dues["total"] = duesTotal
      dues["paid"] = duesPaid
      isValidDues = True
    else:
      messages.showError(
          "Las cuotas que pagaste no pueden ser superiores a las cuotas totales"
      )

    first_iteration = False
  
  return dues

def editDate():
  date = {"day": 0, "month": 0, "year": 0}
  currentYear = datetime.now().year
  first_iteration = True
  while first_iteration or not validateDate.isValidDate(date["day"], date["month"], date["year"], notFuture=True):
    # Fecha del gasto
    date["day"] = validateInputs.inputModel(
        "día del gasto",
        notNull=False,
        isNumber=True,
        isRange=[1, 31],
        defaultValue="Hoy",
        clarification="ENTER- Hoy (predeterminado)",
    )
    if date["day"] != "Hoy":
        date["month"] = validateInputs.inputModel(
            "mes del gasto", isNumber=True, isRange=[1, 12], clear=False
        )
        date["year"] = validateInputs.inputModel(
            "año del gasto",
            isNumber=True,
            isRange=[1900, currentYear],
            clear=False,
        )
    else:
      currentDate = datetime.now()
      date = {
          "day": currentDate.day,
          "month": currentDate.month,
          "year": currentDate.year,
      }

    first_iteration = False
  
  newDate = str(f"{date['year']}-{date['month']}-{date['day']}")
  return newDate

def editInterests():
  interests = validateInputs.inputModel("porcentaje de intereses", isNumber=True, isRange=[0, 100])
  return interests
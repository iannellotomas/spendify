from historic import management
from utilities import validateInputs
from . import editFields
from queries import doQuery
import os

def submenuEdit(idExpense, connectionObj):
  while True:
    os.system("cls")
    print("""
>> EDITAR
← VOLVER (V)
----------------------------------------------
""")
    expense = management.getExpense(idExpense, connectionObj)
    keys = management.showExpenseForEdit(expense, connectionObj)
    print("""
//////////////////////////////////////
""")
    option = input("Ingrese el campo a editar → ")

    if(option == "V"):
      break
    
    if not validateInputs.validateOptionInput(option, len(keys)+1, 1):
      continue
    else:
      field = keys[int(option)]['field']
      editField(field, expense, connectionObj)
    break

def editField(field, expense, connectionObj):
  match field:
    case 'name':

      newName = editFields.editName()
      expense[field] = newName
      updateExpense(field, newName, expense, connectionObj, isString=True)
      enter = input("\nPresione ENTER para volver al historial")

    case 'category':

      newCategoryId = editFields.editCategory(connectionObj)
      updateExpense(field, newCategoryId, expense, connectionObj)
      enter = input("\nPresione ENTER para volver al historial")

    case 'currency':

      newCurrencyId = editFields.editCurrency(connectionObj)
      updateExpense(field, newCurrencyId, expense, connectionObj)
      enter = input("\nPresione ENTER para volver al historial")

    case 'amount':
      
      newAmount = editFields.editAmount()
      updateExpense(field, newAmount, expense, connectionObj)
      enter = input("\nPresione ENTER para volver al historial")

    case 'paymethod':
      
      newPaymethodId = editFields.editPayMethod(connectionObj)
      updateExpense(field, newPaymethodId, expense, connectionObj)
      enter = input("\nPresione ENTER para volver al historial")

    case 'dues':

      newDues = editFields.editDues()
      updateExpense(field, newDues, expense, connectionObj, isDues=True)
      enter = input("\nPresione ENTER para volver al historial")

    case 'interests':

      newInterests = editFields.editInterests()
      updateExpense(field, newInterests, expense, connectionObj)
      enter = input("\nPresione ENTER para volver al historial")

    case 'date':

      newDate = editFields.editDate()
      updateExpense(field, newDate, expense, connectionObj, isString=True)
      enter = input("\nPresione ENTER para volver al historial")


def updateExpense(field, newValue, expense, connectionObj, isString=False, isDues=False):
  translatedFields = {
    "name": "nombre",
    "amount": "monto",
    "category": "id_categoria",
    "currency": "id_moneda",
    "paymethod": "id_metodo",
    "interests": "intereses",
    "date": "fecha",
    "total": "cantidad_cuotas",
    "paid": "cantidad_cuotas_pagas",
    "dues": "cuotas"
  }

  sql = ""

  if isDues:
    sql = f"UPDATE gastos SET {translatedFields['total']} = {int(newValue['total'])}, {translatedFields['paid']} = {int(newValue['paid'])} WHERE id = {expense['id']}"
    doQuery(sql, 'UPDATE', connectionObj)
    return

  if isString:
    sql = f"UPDATE gastos SET {translatedFields[field]} = '{newValue}' WHERE id = {expense['id']}"
  else:
    sql = f"UPDATE gastos SET {translatedFields[field]} = {newValue} WHERE id = {expense['id']}"

  doQuery(sql, 'UPDATE', connectionObj)
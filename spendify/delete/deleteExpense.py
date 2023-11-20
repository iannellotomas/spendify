from queries import doQuery
from historic import management

def deleteExpense(idExpense, connectionObj):
  expense = management.getExpense(idExpense, connectionObj)
  sql = f"DELETE FROM gastos WHERE id = {expense['id']}"
  doQuery(sql, 'DELETE', connectionObj)

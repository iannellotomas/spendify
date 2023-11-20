from queries import doQuery

def resetDB(connectionObj, user):
    sql = f"DELETE * FROM gastos WHERE id_usuario = {user}"
    doQuery(sql, 'DELETE', connectionObj)

    sql = "DELETE * FROM categorias WHERE nombre NOT IN ('Comida', 'Salud', 'Vivienda', 'Entretenimiento')"
    doQuery(sql, 'DELETE', connectionObj)

    sql = "DELETE * FROM metodos WHERE nombre NOT IN ('Efectivo', 'Mercado Pago', 'Tarjeta de Crédito', 'Tarjeta de Débito', 'Transferencia Bancaria')"
    doQuery(sql, 'DELETE', connectionObj)

    sql = f"UPDATE usuarios SET moneda = null, presupuesto = 0, presupuesto_actual = 0 WHERE id = {user}"
    doQuery(sql, 'DELETE', connectionObj)

    print("Se ha restablecido el historial de gastos!")
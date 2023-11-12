from bd import conexion

def doQuery(sql, method, values=0, doReturn = False):

    mycursor = conexion.cursor()  

    match method:
        case 'SELECT':
            if doReturn:
                mycursor.execute(sql)   
                result = mycursor.fetchall()
                print(result)
                return result
        case 'INSERT':
            # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            # La tupla values se reemplaza en %s 
            if values:
                mycursor.execute(sql, values)
                conexion.commit()
                print(mycursor.rowcount, "record inserted.")
        case 'UPDATE':
            mycursor.execute(sql)
            conexion.commit()
            print(mycursor.rowcount, "record(s) affected")
        case 'DELETE':
            mycursor.execute(sql)
            conexion.commit()
            
    return    


    
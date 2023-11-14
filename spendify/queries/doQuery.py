def doQuery(sql, method, connectionObj, values=0, doReturn = False):

    mycursor = connectionObj.cursor()  

    match method:
        case 'SELECT':
            if doReturn:
                mycursor.execute(sql)   
                result = mycursor.fetchall()
                return result
        case 'INSERT':
            # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            # La tupla values se reemplaza en %s 
            if values:
                mycursor.execute(sql, values)
                connectionObj.commit()
                print(mycursor.rowcount, "record inserted.")
        case 'UPDATE':
            mycursor.execute(sql)
            connectionObj.commit()
            print(mycursor.rowcount, "record(s) affected")
        case 'DELETE':
            mycursor.execute(sql)
            connectionObj.commit()
            
    return    


    
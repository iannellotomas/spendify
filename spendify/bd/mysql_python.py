import mysql.connector

# Establecer la conexión

def makeConnection():
  connectionObj = mysql.connector.connect(
      host="bwkh0c2tkz3u5qzmk0yg-mysql.services.clever-cloud.com",
      user="uhjbnvwy1qyailxa",
      password="wjtXaOPPRZW3aPP9WrDi",
      database="bwkh0c2tkz3u5qzmk0yg"
  )

  return connectionObj

def closeConnection(connectionObj):
   connectionObj.close()

def checkConnnection(connectionObj):
  if connectionObj.is_connected():
      print("¡Conexión exitosa!")
      #conexion.close()
  else:
      print("No se pudo conectar")
   

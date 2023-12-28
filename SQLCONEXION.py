import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="19120248",
  database="TSW1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM SERVICIOS")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
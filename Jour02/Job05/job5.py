import mysql.connector
from decimal import Decimal

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="motdepasse1@",
    database="laplateforme"

)


mycursor = mydb.cursor()

sql = "SELECT SUM(`superficie`) FROM `etage`"

mycursor.execute(sql)

myresult = mycursor.fetchone()

print(f"La superficie de La Plateforme est de {myresult[0]} m²")


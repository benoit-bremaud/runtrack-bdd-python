import mysql.connector
from decimal import Decimal

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="motdepasse1@",
    database="laplateforme"

)


mycursor = mydb.cursor()

sql = "SELECT SUM(`capacite`) FROM `salles`"

mycursor.execute(sql)

myresult = mycursor.fetchone()

print(f"La capacité de toutes les salles est de : {myresult[0]}")


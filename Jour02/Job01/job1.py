import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="motdepasse1@",
    database="laplateforme"

)

y =[]
mycursor = mydb.cursor()

mycursor.execute("SELECT `nom`, `capacite` FROM `salles`")

myresult = mycursor.fetchall()

for x in myresult:
    y += (x)

print(y)
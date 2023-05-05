import mysql.connector
from decimal import Decimal

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="motdepasse1@",
    database="laplateforme"

)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE employes (\
    `id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    `nom` VARCHAR(255),\
    `prenom` VARCHAR(255),\
    `salaire` DECIMAL(7,2),\
    `id_service` INTEGER\
    )")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
    
mycursor.execute("INSERT INTO `employes`(`nom`, `prenom`, `salaire`)\
    VALUES\
    ('Bremaud', 'Benoit', 2000.00),\
    ('Berniere', 'Aline', 1900.00),\
    ('Bremaud', 'Louna', 2500.00),\
    ('Vial', 'Anne-Marie', 2800.00),\
    ('Dupond', 'Moretti', 3000.00),\
    ('Brad', 'Pitt', 3500.00);\
    ")

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM `employes`\
    -> WHERE `salaire` > 3000.00;")
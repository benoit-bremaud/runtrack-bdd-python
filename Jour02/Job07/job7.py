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

# Requête permettant de récupérer tout les employés dont le salaire > 3000€
mycursor.execute("SELECT * FROM `employes`\
    -> WHERE `salaire` > 3000.00;")

# MAJ fichier

# maj

# Ajout d'une table `services` contenant les champs `id` et `nom`
mycursor.execute("CREATE TABLE `services` (\
    `id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    `nom` VARCHAR(255)\
    )")

# Inserer de nom de service dans table `services` 
mycursor.execute("INSERT INTO `services` (`nom`)\
    VALUES\
    ('Comptabilité'),\
    ('Administratif),\
    ('Technique'),\
    ('RH'),\
    ('ADV'),\
    ('Production'),\
    ('Méthode'),\
    ('Qualité')\
    ")

# Mettre à jour le champ `id_service` la table `employés`
# for i in range(1, 7, 1):

for i in range(1, 7, 1):
    sql = f"UPDATE `employes` SET `id_service` = {i} WHERE `id` = {i}"
    mycursor.execute(sql)

mydb.commit()

# Récupère les employés et leur service respectif

sql = "SELECT * FROM `employes` JOIN `services` ON `employes`.`id_service` = `services`.`id`"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


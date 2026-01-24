import sqlite3
 
conect = sqlite3.connect('database.db')
c = conect.cursor()

c.execute("CREATE TABLE IF NOT EXISTS usuario(id integer,nome text,idade number)")


c.execute("INSERT INTO usuario Values(1,'Samuel',19)")
c.execute("INSERT INTO usuario Values(2,'Sara',20)")

print(c.execute("SELECT*FROM usuario WHERE nome='Samuel'"))

conect.commit()

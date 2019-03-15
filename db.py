import sqlite3

con=sqlite3.connect("QUALITY OF LIVING CITY RANKING.db")
cursor=con.cursor()

def creat_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS book(Ranking INT, City TEXT, Country TEXT)")
    con.commit()

def add_data():
    cursor.execute("INSERT INTO book Values(1,'Vienna', 'Austria')")
    cursor.execute("INSERT INTO book Values(2,'Zurich', 'Switzerland')")
    cursor.execute("INSERT INTO book Values(3,'Vancouver', 'Canada')")
    cursor.execute("INSERT INTO book Values(4,'Munich', 'Germany')")
    cursor.execute("INSERT INTO book Values(5,'Auckland', 'New Zealand')")
    cursor.execute("INSERT INTO book Values(6,'Dusseldorf', 'Germany')")
    cursor.execute("INSERT INTO book Values(7,'Frankfurt', 'Germany')")
    cursor.execute("INSERT INTO book Values(8,'Copenhagen', 'Denmark')")
    cursor.execute("INSERT INTO book Values(9,'Geneva', 'Switzerland')")
    cursor.execute("INSERT INTO book Values(10,'Basel', 'Switzerland')")
    cursor.execute("INSERT INTO book Values(11,'Amsterdam', 'Netherlands')")

    con.commit()


creat_table()
add_data()
con.close()



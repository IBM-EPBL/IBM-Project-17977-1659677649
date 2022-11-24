import sqlite3 as sql
conn=sql.connect('Rec.db')
print("Opened database successfully")
conn.execute('CREATE TABLE signup(Email TEXT, Name TEXT, Password TEXT, Conform_Password TEXT)')
conn.execute('CREATE TABLE login(Email TEXT, Password TEXT)')
conn.execute('CREATE TABLE contact(Name TEXT, Email TEXT, Subject TEXT, Number INTEGER, Message TEXT)')
conn.execute('CREATE TABLE Buy(Name TEXT, Email TEXT, Address TEXT, Number INTEGER, Payment TEXT, Product INTEGER)')
print("table created successfully")
conn.close()

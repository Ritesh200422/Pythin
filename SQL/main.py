import sqlite3
conn = sqlite3.connect('test.db')
# print("opened Data Base Sucessfilly")
#
# conn.execute('''CREATE TABLE Company(
#         ID INT PRIMARY KEY NOT NULL,
#         NAME TEXT NOT NULL,
#         AGE INT NOT NULL,
#         ADDRESS CHAR(50),
#         SALARY REAL);''')
# print("Table Created successfully")
cur = conn.cursor()
cur.execute('''INSERT INTO company VALUES
(20,'RITESH',19, 'LN NAGAR',21000),(12,'MANOJ',30,'RAMTIRTHA',22000)
 ''')

new =cur.execute('SELECT * FROM company')
conn.commit()
new.fetchall()

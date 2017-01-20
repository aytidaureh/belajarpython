import mysql.connector as mdb

print('connecting to mysql server...')

cnx = mdb.connect(user='root',

                              password='',

                              host='127.0.0.1',

                              database='python')
Eksekusi = cnx.cursor()
result = Eksekusi.fetchone()

if result != 0:
	prin('berhasil')
else:
	print('gagal')

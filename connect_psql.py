import psycopg2  # pip install pyscopg2

con=psycopg2.connect(
      host= 'localhost' ,
      port= '5432' ,
      user= 'postgres' ,
      password= 'lungmaker'
)

cur = con.cursor()

# select command
cur.execute('select * from package limit 5;')
print(cur.fetchall())

con.commit()
cur.close()

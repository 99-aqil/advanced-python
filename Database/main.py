import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="root", port=5432)

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")

cursor.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'Aqil', 24, 'M'),
(2, 'Sanjida', 23, 'F'),
(3, 'Raquib', 26, 'M'),
(4, 'Zobayda', 27, 'F'),
(5, 'Abid', 22, 'M');
""")

cursor.execute("""SELECT * FROM person WHERE name = 'Raquib';""")
print(cursor.fetchone())

cursor.execute("""SELECT * FROM person WHERE age < 50;""")
for row in cursor.fetchall():
    print(row)


sql = cursor.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("A", 50))
print(sql)
cursor.execute(sql)
print(cursor.fetchall())

connection.commit()

cursor.close()
connection.close()

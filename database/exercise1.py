import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS employees(
               id INTEGER NOT NULL PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER NOT NULL,
               department TEXT NOT NULL
               
               
               )



''')

# cursor.executemany("INSERT INTO employees(id,name,age,department)VALUES(?,?,?,?)",[
#                     (1, 'Ali', 25, 'HR'),
#                     (2, 'John', 30, 'Engineering'),
#                     (3, 'Mary', 28, 'Marketing')

# ])









cursor.execute('''
    UPDATE employees
    SET department = "Finance"
    WHERE id = 3

''')


cursor.execute('''
    SELECT * FROM employees
    WHERE department = "Engineering"

''')
# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    WHERE age > 26

''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    WHERE id = 2


''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * from employees
    ORDER BY age ASC
''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    ORDER BY age DESC
    LIMIT 1

''')
# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    WHERE name LIKE 'M%'

''')
# for row in cursor.fetchall():
#     print(row)
cursor.execute('''
    SELECT * FROM employees
    WHERE department LIKE '%ing'
''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    ORDER BY name ASC
    LIMIT 2
''')


cursor.execute('''
    SELECT * FROM employees
    WHERE age > 25 AND department = "Engineering"

''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    WHERE department = 'HR' OR department ='Finance'

''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    SELECT * FROM employees
    WHERE age < 30 AND (name LIKE "A%" OR name LIKE 'M%')

''')

# for row in cursor.fetchall():
#     print(row)


cursor.execute('''
    DELETE FROM employees
    WHERE name = "Ali"

''')
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

cursor.execute('''
    DELETE FROM employees
    WHERE department = 'Finance'
''')
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)


conn.commit()
conn.close()
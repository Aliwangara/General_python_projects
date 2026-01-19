import sqlite3

conn = sqlite3.connect("company_management_system/company_system.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
               id INTEGER PRIMARY KEY NOT NULL,
               name TEXT NOT NULL,
               department TEXT NOT NULL
               )

''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments(
               id INTEGER PRIMARY KEY NOT NULL,
               name TEXT NOT NULL
               )

''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS salaries(
               id INTEGER PRIMARY KEY NOT NULL,
               employee_id INTEGER NOT NULL,
               amount REAL NOT NULL
               )

''')

# cursor.executemany("INSERT INTO departments(id,name)VALUES(?,?)",[(1, 'Engineering'),
# (2, 'Finance'),
# (3, 'Human Resources')])

# cursor.executemany("INSERT INTO employees(id,name,department)VALUES(?,?,?)",[(1, 'Ali Ahmed', 'Engineering'),
# (2, 'Fatima Noor', 'Finance'),
# (3, 'John Mwangi', 'Engineering'),
# (4, 'Mary Wanjiku', 'Human Resources'),
# (5, 'David Kimani', 'Finance')])

# cursor.executemany("INSERT INTO salaries(id,employee_id,amount)VALUES(?,?,?)",[(1, 1, 70000),
# (2, 2, 85000),
# (3, 3, 75000),
# (4, 4, 60000),
# (5, 5, 90000)])

cursor.execute("SELECT * FROM employees")

cursor.execute('''
    SELECT name,department FROM employees
    
''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute('''
    select * FROM employees
    WHERE age > 30

''')


cursor.execute('''
    select * FROM employees
    WHERE department = "HR" OR department = "Engineering"

''')

cursor.execute('''
    select * FROM employees
    WHERE name LIKE '%A' OR name LIKE '%M'

''')

cursor.execute('''
    SELECT * FROM employees
    ORDER BY age ASC
    LIMIT 1

''')
cursor.execute('''
    SELECT * FROM employees
    ORDER BY age DESC

''')

cursor.execute('''
    UPDATE employees
    SET department = "Business"
    WHERE name = "Fatima Noor"

''')
cursor.execute('''
    UPDATE salaries
    SET amount = 20000.00
    WHERE id = 1

''')

cursor.execute('''
    DELETE employees
    WHERE name = "Mary Wanjiku"

''')
cursor.execute('''
    DELETE employees
    WHERE department = "Finance"

''')

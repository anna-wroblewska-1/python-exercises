# Expense Tracker
# Track daily expenses and categorize them:

# Add, edit, and delete expenses.
# Categorize expenses (food, transport, entertainment, etc.).
# Summarize expenses over a period.

# id SERIAL PRIMARY KEY,
# date DATE NOT NULL,
# amount DECIMAL(10, 2) NOT NULL,
# category VARCHAR(50) NOT NULL,

import psycopg2

conn = psycopg2.connect(database="Expense_tracker",
                        host="localhost",
                        user="postgres",
                        password="Elefan7",
                        port="5432")

cursor = conn.cursor()
cursor.execute('SELECT * FROM Expense_tracker ORDER BY id')


#chyba trzeba jednak budować klasę i zapisać do csv.file?


#drugi pomysł
def add_expense():
    amount = input(print("How much did you spent?"))
    category = input("In which category?\n1.Food\n2.Fun\n3.Health\n4.Other")
    cursor.execute(f'''
                   INSERT INTO Expense_tracker(amount, category)
                   VALUES ('{amount}', '{category}')
                   ''')
def edit_expense():
    to_edit = input(print("Which to edit? "))



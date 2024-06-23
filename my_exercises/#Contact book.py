#Contact book
#Add, update, delete, and search contacts.
#Store contacts in a file or database.
#Load contacts at startup and save changes when exiting.

import psycopg2

conn = psycopg2.connect(database="contact_book",
                        host="localhost",
                        user="postgres",
                        password="Elefan7",
                        port="5432")

cursor = conn.cursor()
cursor.execute('SELECT * FROM contact_book ORDER BY id')

contacts = cursor.fetchall()
print("Your Contact Book:\n")
for row in contacts:
    print(row)

def adding_name(add_name, add_number):
    add_name = input(print("Write name to add: "))
    add_number = input(print("Write number to add: "))
    cursor.execute(f'''
                   INSERT INTO contact_book(name, phone)
                   VALUES ('{add_name}', '{add_number}')
                   ''')
    
def updating():
    id_to_update = input(print("Select contact id to update: "))
    name_or_phone = input(print("What you want to change?\n 1.Name \n 2.Phone: \n 3.Both "))
    if name_or_phone == "1":
        update_name = input(print("Write new name: "))
        cursor.execute(f'''
                UPDATE contact_book
                SET name = '{update_name}'
                WHERE id = {id_to_update}
                ''')
    elif name_or_phone == "2":
        update_number = input(print("Write new number: "))
        cursor.execute(f'''
                UPDATE contact_book
                SET phone = '{update_number}'
                WHERE id = {id_to_update}
                ''')
    elif name_or_phone =="3":
        update_name = input(print("Write new name: "))
        update_number = input(print("Write new number: "))
        cursor.execute(f'''
                UPDATE contact_book
                SET name = '{update_name}', phone = '{update_number}'
                WHERE id = {id_to_update}
                ''')
    else:
        print("Don't play with me!")

def deleting():
    id_to_delete = input(print("Which id to delete?"))
    cursor.execute(f'''
        DELETE FROM contact_book WHERE id = {id_to_delete}
    ''')

    cursor.execute('''
        WITH updated AS (
        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
        FROM contact_book
    )
    UPDATE contact_book
    SET id = updated.new_id
    FROM updated
    WHERE contact_book.id = updated.id;
    ''')

    cursor.execute('''
    SELECT setval('contact_book_id_seq', (SELECT MAX(id) FROM contact_book));
    ''')

    print("Your contact boook now:\n")
    contacts = cursor.fetchall()
    for row in contacts:
        print(row)

choice = input(print("What do you want to do, choose:\n 1. Add contact \n 2. Update \n 3. Delete \n 4. Search \n"))

if choice == "1":
    adding_name()

if choice == "2":
    updating()

if choice == "3":
    deleting()

if choice == "4":
    search = input(print("What name are you searching for?"))
    print("Your search:\n")
    cursor.execute(f'''
                   SELECT id, name, phone FROM contact_book
                   WHERE name = '{search}'
                   ''')


conn.commit()
conn.close()
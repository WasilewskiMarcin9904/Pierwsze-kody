import sqlite3
                            # skrót db od datdabase
connection = sqlite3.connect("todo.db")

def create_table(connection):
    try:
        #  pobieramy kursor (niezbędne)
        cur = connection.cursor()
        #   wywołujemy na kursorze execute ( stworz tabele o nazwie TASK (kolumny w tabeli (kolumna o nazwie "task" i typu tekstowego)))
        cur.execute("""CREATE TABLE task(task tekst)""")
    except:
        pass

def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowiID, task FROM task""")
    result = cur.fetchall()

    for row in result:
        # row 0 w tym przypadku to rowID a row 1 to task (zadanie)
        print(str(row[0]) + " - " + row[1])

def add_task(connection):
    task = input("Wpisz treść zadania: ")
    if task == "0":
        print("Powrót do menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,) )
        connection.commit()
    print("Dodano zadanie!")


def delete_task(connection):
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowID=?""", (task_index,)).rowcount
    connection.commit()
    if rows_deleted == 0:
        print("Takie zadanie nie istnieje")
    else:
        print("Usunięto zadanie!")

create_table(connection)
while True:
    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()
    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

connection.close()
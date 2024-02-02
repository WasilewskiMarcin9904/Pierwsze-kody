import json
user_choice = 0

def save_name_to_file():
    dictionary_of_name = {"nazwa_pliku":file_name}
    with open("Nazwa_pliku_użytkownika.json", "w") as file:
        json.dump(dictionary_of_name, file)

def load_file_name():
    try:
        with open("Nazwa_pliku_użytkownika.json", "r") as file:
            load_file = json.load(file)
            load_name = load_file["nazwa_pliku"]
            return load_name
    except FileNotFoundError:
        return None

file_name = load_file_name()
if file_name:
    print("Nazwałeś juz plik:", file_name )
else:
    file_name = input("Wprowadź nazwę pliku do którego będziesz zapisywał zadania: ")
    save_name_to_file()


tasks = []
completed_tasks = []
current_tasks = []
bin = []

def show_tasks():
    task_index = -1
    print()
    print("\nWszystkie zadania: \n")
    print()
    for task in tasks:
        task_index +=1
        print("Nr:", "[", str(task_index) ,"]",  task )
        print()
    print()
    print("Bierzące zadania: ")
    print()
    for task in current_tasks:
        task_index = -1
        task_index += 1
        print("Nr:", "[", str(task_index) ,"]",  task )
        print()
    print()
    print("Wykonane zadania: ")
    print()
    for task in completed_tasks:
        task_index = -1
        task_index += 1
        print("Nr:", "[", str(task_index) ,"]",  task )
        print()

def add_task():
    add_task = input("Napisz treść zadania: ")
    tasks.append(add_task)
    print()
    print("Zadanie zostało dodane")
    print()

def delete_task():
    task_index = -1
    pop = int(input("Które z zadań chcesz usunąć?: "))
    if pop > len(tasks) or pop < 0:
        print()
        print("Błędne polecenie")
        print()
    print()
    for _ in tasks:
        task_index = tasks[pop]
    print()
    print("Usunięto zadanie:", task_index)   
    print()
    bin.append(task_index)
    tasks.pop(pop)

def to_completed_task():
    pop = int(input("Które z zadań chcesz oznaczyć jako zakończone?: "))
    if pop > len(tasks) or pop < 0:
        print()
        print("Błędne polecenie")
        print()
    print()
    for _ in tasks:
        task_completed = tasks[pop]
    print("Zakończone zadanie:", task_completed)
    completed_tasks.append(task_completed)    
    tasks.pop(pop)
    try:
        current_tasks.pop(pop)
    except IndexError:
        return 

def save_task_to_file():
    global file_name
    zadania_json = {
    "Wszystkie_zadania":tasks,
    "Zadania_do_wykonania":current_tasks,
    "Zakonczone_zadania":completed_tasks
    }
    with open(file_name + '.json', 'w') as plik:
        json.dump(zadania_json, plik)



def load_tasks_from_file():
    global file_name
    try:
        with open(file_name + '.json', 'r') as plik:
            zadania = json.load(plik)
            al_tasks = zadania["Wszystkie_zadania"]
            for task in al_tasks:
                tasks.append(task + "\n")
            current_task = zadania["Zadania_do_wykonania"]
            for task in current_task:
                current_tasks.append(task + "\n")   
            completed_task = zadania["Zakonczone_zadania"]
            for task in completed_task:
                completed_tasks.append(task + "\n")
    except FileNotFoundError:
        return None
    
def to_do_taks_to_current_tasks():
    try:
        current_choice = int(input("Które zadanie chcesz oznaczyć za bierzące?: "))
        if current_choice < 0 or current_choice > len(tasks):
            print()
            print("Błędne polecenie, spróbuj jeszcze raz")
            print()
        
        choice = tasks[current_choice]
        current_tasks.append(choice)
    except ValueError:
        print()
        print("Błędne polecenie, spróbuj jeszcze raz")
        print()
    
def show_current_tasks():
    task_index = -1
    print()
    print("Zadania do wykonania: ")
    print()
    for task in current_tasks:
        task_index +=1
        print("Nr:", "[", str(task_index) ,"]",  task )
        print()

def show_completed_tasks():
    task_index = -1
    print()
    print("Zakończone zadania: ")
    print()
    for task in completed_tasks:
        task_index +=1
        print("Nr:", "[", str(task_index) ,"]",  task )
        print()

def empty_the_trash():
    bin.clear()
    print("Kosz został opróżniony")

def restore_task():
    task_index = 0
    for task in bin:
        print()
        print("Nr", " [", task_index, "] ", task)
        print()
        task_index += 1
        restore = int(input("Które zadanie chcesz odzyskać?: "))
        tasks_index = bin[restore]
    tasks.append(tasks_index)
    bin.pop(restore)



load_tasks_from_file()
while user_choice != 10:
    
    if user_choice < 0:
        print()
        print("Błędne polecenie")  
        print()  
    if user_choice > 10:
        print()
        print("Błędne polecenie")
        print()
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        show_current_tasks()
    if user_choice == 3:
        show_completed_tasks()
    if user_choice == 4:
        add_task()
    if user_choice == 5:
        delete_task()
    if user_choice == 6:
        to_do_taks_to_current_tasks()
    if user_choice == 7:
        to_completed_task()
    if user_choice == 8:
        save_task_to_file()
    if user_choice == 9:
        print("Kosz")
        choice = -1
        while choice != 3:
            if choice > 3:
                print()
                print("Błędne polecenie")
                print()
            if choice <= 0:
                print()
                print("Błędne polecenie")
                print()
            if choice == 1:
                empty_the_trash()
            if choice == 2:
                restore_task()
            task_index = 0
            for task in bin:
                print()
                print("Nr", " [", task_index, "] ", task)
                print()
                task_index += 1
            print()
            print("1. Oprożnij kosz")
            print("2. Przywróć zadanie")
            print("3. Powrót do menu głownego")
            print()
            try:
                choice = int(input("Co chcesz zrobić: "))
            except ValueError:
                print("TYLKO LICZBY! ")

    print("1. Wyświetl wszystkie zadania")
    print("2. Wyświetl same bierzące zadania")
    print("3. Wyświetl same zakończone zadania")
    print("4. Dodaj zadanie")
    print("5. Usuń zadanie")
    print("6. Oznacz zadanie jako bierzące")
    print("7. Oznacz zadanie jako zakończone")
    print("8. Zapisz zadania do pliku")
    print("9. Kosz")
    print("10. Wyjdź")

    print()
    try:
        user_choice = int(input("Wybierz, co chcesz zrobić: "))
        print()
    except ValueError:
        print()
        print("MOŻNA WPISAĆ TYLKO LICZBĘ!")
        print()

expenses = []
months = {1:"Styczeń", 2:"Luty", 3:"Marzec", 4:"Kwiecień", 5:"Maj", 6:"Czerwiec", 7:"Lipiec", 8:"Sierpień", 9:"Wrzesień", 10:"Październik", 11:"Listopad", 12:"Grudzień"}

def show_expenses(month):
    highest_expense = []
    # print(expenses)                   month -> expense_month
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')  
    # sorted_expenses = quickSort([expense_amount for expense_amount,_,_ in expenses if expense_month == month])     
    # print("Wydatki od najwyższego:")
    # for expense_amount in sorted_expenses:
    #     expense_type = [expense_type for amount, expense_type, expense_month in expenses if amount == expense_amount and expense_month == month][0]
    #     print(f'{expense_amount} - {expense_type}')
    sorted_expenses = quickSort([(amount, expense_type, expense_month) for amount, expense_type, expense_month in expenses if expense_month == month])     
    print("Najwyższy wydatek tego miesiąca:")
    for expense_amount, expense_type, _ in sorted_expenses:
        highest_expense.append(expense_amount)
    print(f'{highest_expense[0]} - {expense_type}')

def add_expense(month):
    print()
    expense_amount = int(input("Podaj kwotę [zł]: "))
    while True:
        expense_type = input("Podaj typ wydatku (Jedzenie, rozrywka, dom, inny): ") 
        if expense_type.isalpha():
            expense = (expense_amount, expense_type, month)
            expenses.append(expense)
            break
        else:
            print("Wprowadź poprawny typ wydatku")
#                              sumujemy expesne_amount dla takiej pętli for , jeżeli wydatek tyczy sie miesiąca o którego pytamy 
def show_stats(month):
    total_amount_this_mount = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_mount = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expense_this_month = total_amount_this_mount / number_of_expenses_this_mount
    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_all = total_amount_all / len(expenses)
    
    print()
    print("Statystyki")
    print("Wszystkie wydatki wtym miesiącu [zł]:", total_amount_this_mount)
    print("Średni wydatek w tym miesiącu [zł]:",  average_expense_this_month)
    print("Wszystkie wydatki [zł]:", total_amount_all)
    print("Średni wydatek [zł]:", average_expense_all)
    
def quickSort(data_month):
    if len(data_month) > 1:
        return quickSort([x for x in data_month[1:] if x > data_month[0]]) + [x for x in data_month if x == data_month[0]] + ([x for x in data_month[1:] if x < data_month[0]])
    else:
        return data_month


while True:
    print()
    while True:
        try:
            month = int(input("Wybierz miesiąc [1-12]:"))
            if 1 <= month <= 12:
                break
                
            elif month == 0:
                break
            else:
                print("Wprowadź poprawną liczbę.")
        except ValueError:
            print("Wprowadź poprawną liczbę.")
            

    while True:
        print(f"\nMiesiąc: {months[month]}")
        print()
        print("0. Powrót do wyboru miesiąca")
        print("1. Wyświetl wszystkie wydatki")
        print("2. Dodaj wydatek")
        print("3. Statystyka")
        try:
            choice = int(input("Wybierz opcje: "))

            if choice == 0:
                break

            if choice == 1:
                # print("Wszystkie wydatki")
                show_expenses(month)

            if choice == 2:
                # print("Dodaj wyatki")
                add_expense(month)

            if choice == 3:
                show_stats(month)
            elif choice > 3:
                print("Wprowadź liczbe z przedziału 1-3")
        except ValueError:
            print("Wprowadź poprawną liczbę.")
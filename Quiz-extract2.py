import json
import random
import sys
from termcolor import colored
points = 0
fifty_fifty_used = False


def lvl_choice():
    global points
    
    while questions:
        print("\nPoziomy trudności: \n1.Łatwy\n2.Średni\n3.Trudny\nᴊᴇśʟɪ ᴄʜᴄᴇsᴢ ᴡʏśᴡɪᴇᴛʟɪć ʀᴀɴᴋɪɴɢ ɢʀᴀᴄᴢʏ ᴡᴄɪsɴɪᴊ (9)")
        level_choice = input("\nWybierz poziom trudności: ")

        if level_choice == '9':  
            show_ranking(points)

        try:
            level_choice = int(level_choice)
            if 0 < level_choice < 4:
                break
            else:
                print("\nWybierz liczbę między 1 a 3.")

        except ValueError:
            print("\nWpisz liczbę określającą poziom trudności.")
        
    try:
        if level_choice == 1:
            easy_questions = questions["easy"]
            while easy_questions:
                random_easy_question = random.choice(easy_questions)
                show_questions(random_easy_question, level_choice)
                easy_questions.remove(random_easy_question)
            else:
                print("Brak pytań w wybranym poziomie trudności.")
                del questions["easy"]
                lvl_choice()
        elif level_choice == 2:
            medium_questions = questions["medium"]
            while medium_questions:
                random_medium_question = random.choice(medium_questions)
                show_questions(random_medium_question, level_choice)
                medium_questions.remove(random_medium_question)
            else:
                print("Brak pytań w wybranym poziomie trudności.")
                del questions["medium"]
                lvl_choice()
        elif level_choice == 3:
            hard_questions = questions["hard"]
            while hard_questions:
                random_hard_question = random.choice(hard_questions)
                show_questions(random_hard_question,level_choice)
                hard_questions.remove(random_hard_question)
            else:
                print("Brak pytań w wybranym poziomie trudności.")
                del questions["hard"]
                lvl_choice()
        return level_choice
    
    except KeyError:
        print(" ! Brak pytań w wybranym poziomie trudności ! ")
        lvl_choice()

def quicksort(data):
    if len(data) > 1:
        return quicksort([x for x in data[1:] if x < data[0]]) + [x for x in data if x == data[0]] + quicksort([x for x in data[1:] if x > data[0]])
    else:
        return data
    
def show_ranking(points):
    with open('ranking.txt', 'r') as file:
        lines = file.readlines()
    # Tworzenie listy krotek z odczytanych danych
    data = []
    for line in lines:
        # Przyjmujemy format: "Gracz: Nazwa Pkt: Punkty"
        parts = [word.replace(',', '').replace("'", '') for word in line.split()]
        player = parts[1]
        points = parts[3]
        data.append((player, points))
        
    # Sortowanie danych od najwyższej do najniższej ilości punktów
    posortowane_dane = quicksort(data)

    # Wyświetlanie posortowanego rankingu
    for pozycja, (gracz, punkty) in enumerate(posortowane_dane, start=1):
        szerokosc_kolumny_gracz = 25
        szerokosc_kolumny_punkty = 10
        formatowany_napis = f"{pozycja}. Gracz: \033[1m{gracz:<{szerokosc_kolumny_gracz}}\033[0m Punkty: \033[1m{punkty:<{szerokosc_kolumny_punkty}}\033[0m"
        print(formatowany_napis)
        # print(f"{pozycja}. Gracz: \033[1m{gracz}\033[0m Punkty: \033[1m{punkty}\033[0m")

def fifty_fifty(question):
    global fifty_fifty_used

    if fifty_fifty_used:
        print("\nOpcja '50:50' została już wykorzystana.")
        return
    
    # błedne odpowiedzi = lista[opcji które które zawieraja sie w "abcd" jeżeli ta opcja nie jest prawidłowa odpowiedzią]
    incorrect_answers = [option for option in "abcd" if option != question["prawidlowa_odpowiedz"]]

    # Jeżeli błędnych odpowiedzi jest mniej niż 2 nie wykonuj fifty_fifty
    if len(incorrect_answers) < 2:
        print("Nie można zastosować tej podpowiedzi ponownie.")
        return
    # do usunięcia = losowy wybór błędnej odpowiedzi, 2x
    to_remove = random.sample(incorrect_answers, 2)

    options = {
        "a":question["a"],
        "b":question["b"],
        "c":question["c"],
        "d":question["d"]

    }
    # dla błednych odpowiedzi w słowniku {options} zamień na pustego stringa (żeby nie wyświetlało tych nieporawidlowych odpowiedzi)
    for incorrect_answer in to_remove:
        options[incorrect_answer] = ""
        
    # dla "a", question["a"] 
    for option, answer in options.items():
        if answer:
            print(f"{option} {answer}")

    fifty_fifty_used = True

def show_questions(question, level_choice):
    
    global points
    print()
    print(question["pytanie"])
    print("a", question["a"])
    print("b", question["b"])
    print("c", question["c"])
    print("d", question["d"])
    print()

    while questions:
        print("ᴊᴇśʟɪ ᴄʜᴄᴇsᴢ ᴢᴍɪᴇɴɪć ᴘᴏᴢɪᴏᴍ ᴛʀᴜᴅɴᴏśᴄɪ ᴡᴄɪsɴɪᴊ (0)\nᴊᴇśli ᴄʜᴄᴇsᴢ ᴜżʏᴄ ᴏᴘᴄᴊɪ '50:50' ᴡᴄɪsɴɪᴊ (9)\n")
        answer = input("Którą odpowiedź wybierasz?: ")
        
        if answer in ["a", "b", "c", "d"]:
            break
        elif answer in [str(0)]:
                lvl_choice()
        elif answer in [str(9)]:
            fifty_fifty(question)
        else:
            print("Wybierz odpowiedź pośród liter (a) (b) (c) (d)")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1 if level_choice == 1 else 2 if level_choice == 2 else 3 

        print("\nTo prawidłowa odpowiedź, Brawo!, Masz już", points, "Pkt")
    
    else:
        print("Niestety to zła odpowiedź. Prawidłowa odpowiedź to:", question["prawidlowa_odpowiedz"])
    
    
player = input("Wpisz nazwe użytkownika: ")

with open ("quiz2.json") as file:
    questions = json.load(file)
try:
    lvl_choice()
    
except UnboundLocalError:
    print("\nKoniec gry. Zdobyłeś", points, "punktów!")
    player_stats = {"Gracz": player, "Punkty": int(points)}
    with open('ranking.txt', "a") as file:
        file.write(f"Gracz: {player_stats['Gracz']} Punkty: {player_stats['Punkty']}\n")
    sys.exit(0)

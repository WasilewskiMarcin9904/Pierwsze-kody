import sys
import random
from termcolor import colored
# from getpass import getpass
pkt = 0
nouns = []    


no_of_tries = 15


with open("jezyk-polski-slowniki\class_a.txt", "r") as file:
    for line in file.readlines():
        lines = line.split(";")
        nouns.append(lines[0])

    

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


def show_state_of_game(user_word, used_letters, no_of_tries):
    print(f"""\n{user_word}\nUżyte litery: {used_letters}""")
    if 16 > no_of_tries > 9:
        print(f"\nPozostało prób: \033[1;32m{no_of_tries}\033[0m")
    elif 10 > no_of_tries > 4:
        print(f"\nPozostało prób: \033[33m{no_of_tries}\033[0m")
    else:
        print(f"\nPozostało prób: \033[1;91m{no_of_tries}\033[0m")

def select_difficulty(diff_choice):
    
    if diff_choice == 1:
        easy_words = [noun for noun in nouns if len(noun) <= 4]
        return random.choice(easy_words) if easy_words else random.choice(nouns)
    elif diff_choice == 2:
        medium_words = [noun for noun in nouns if 4 < len(noun) <= 7]
        return random.choice(medium_words) if medium_words else random.choice(nouns)
    elif diff_choice == 3:
        hard_words = [noun for noun in nouns if len(noun) > 7]
        return random.choice(hard_words) if hard_words else random.choice(nouns)
    else:
        print("Niepoprawny wybór poziomu trudności. Wybieram losowo.")
        return random.choice(nouns)


  

def gra(diff_choice):
    global pkt
    global no_of_tries
    user_word = []
    used_letters = []
    
    word = select_difficulty(diff_choice)
    

    if word:
        print("""\n1.Kontynuj z takim samym poziomem trudności\n2.Zmień poziom trudności""")
        user_choice = int(input("\nCo chcesz zrobić?: "))

        if user_choice == 1:
            print("\n(Poziom pozostał taki sam)")
        elif user_choice == 2:
            print(f"\nPoziomy:\033[1;32m\n1.Łatwy\033[0m\033[33m\n2.Średni\033[0m\033[1;91m\n3.Trudny\033[0m")
            new_diff_choice = int(input("\nWybierz nowy poziom trudności: "))
            diff_choice = new_diff_choice  # Aktualizacja wartości diff_choice na nowy wybór użytkownika

    word = select_difficulty(diff_choice)
    
    for _ in word:
        user_word.append("_")
    
    while user_word != word:
            

        show_state_of_game(user_word, used_letters, no_of_tries)
        
        letter = input("\nPodaj literę: \n").strip()
        # letter = getpass("\nPodaj literę: ").strip()

        found_indexes = (find_indexes(word, letter))

        if letter.isalpha() and len(letter) == 1:
            if len(found_indexes) > 0:
                    print(f"\033[1;32m\nDobrze!\n\033[0m")
            else:
                    print(f"\033[1;91mŹle :(\033[0m")
        else:
            print(f"\n\033[1;91mBłąd! Wprowadź tylko litery!\033[0m\n")
            no_of_tries += 0
            
        print(word)
            
        if len(found_indexes) == 0 and letter.isalpha():
            print(f"\033[33mNie ma takiej litery: [{letter}]\033[0m") 
            if len(found_indexes) == 0 and letter not in used_letters and len(letter) == 1:
                no_of_tries -= 1
                used_letters.extend(letter) 
                
            if no_of_tries == 0:
                print(f"""\nKoniec gry :(\nZdobyłeś łącznie: \033[1m{pkt}\033[0m pkt\n""")
                sys.exit(0)
        else:
            if letter in used_letters:
                no_of_tries -= 0
            for index in found_indexes:
                user_word[index] = letter
                
            if "".join(user_word) == word:
                print(f"Brawo to jest to słowo!: \033[32m{word}\033[0m")
                if len(word) <= 4:
                    pkt += 1
                if 4 < len(word) <= 7:
                    pkt += 2
                if len(word) > 7:
                    pkt += 3
                print(f"Masz już \033[1m{pkt}\033[0m pkt")
                nouns.remove(word)

                gra(diff_choice)
                

print(f"\nPoziomy:\033[1;32m\n1.Łatwy\033[0m\033[33m\n2.Średni\033[0m\033[1;91m\n3.Trudny\033[0m")
while True:
    try:
        diff_choice = int(input("\nWybierz poziom trudności: "))
        gra(diff_choice)
    except ValueError:
        print("Wprowadź liczbę odpowiadającą poziomowi trudności.")

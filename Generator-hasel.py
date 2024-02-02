import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left
    
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków spoza przedziału 0,", characters_left)            
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)
            
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Proszę wprowadzić liczbę.")
def stats():
    print(f"\nDługość hasła: {password_length}\nMałe litery: {lowercase_letter}\nDuże litery: {uppercase_letters}\nZnaki specjalne: {special_characters}\nCyfry: {digits}\n")

def get_valid_characters(prompt):
    while True:
        value = get_valid_input(prompt)
        if value >= 0 and value <= characters_left:
            return value
        else:
            print("Nieprawidłowa wartość. Proszę spróbować ponownie.")

while True:
    password_length = get_valid_input("Ile znaków ma mieć hasło: ")

    if password_length < 5:
        print("Hasło musi mieć minimum 5 znaków, podaj wiekszą liczbę.")
        
    else:
        characters_left = password_length
        break

lowercase_letter = get_valid_characters("Ile małych liter ma mieć hasło?: ")
update_characters_left(lowercase_letter)
uppercase_letters = get_valid_characters("Ile dużych liter ma mieć hasło?: ")
update_characters_left(uppercase_letters)
special_characters = get_valid_characters("Ile znaków specjalnych ma mieć hasło?: ")
update_characters_left(special_characters)
digits = get_valid_characters("Ile cyfr ma mieć hasło?: ")
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki wykorzystane - Uzupełnienie małymi literami")
    lowercase_letter += characters_left



stats()
# PĘTLA FOR WYKONA SIE TYLE RAZY ILE MAMY ZNAKÓW W HAŚLE!!!!!!!!!!!!!
# Dla liczby w zakresie(długości hasła):
#   jezeli małe litery > 0
# dodaj do listy hasła randomowy wybór z małych liter 
#  zabierz z liczby dostepnych małych liter 1
for _ in range(password_length):
    if lowercase_letter > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letter -= 1 
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1 
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1 

random.shuffle(password)
print("Wygenerowane hasło:", "".join(password))


# mozna również zastosowac prostrzą wersje:

# import random 
# import string

# password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(int(input("Ile znaków ma miec hasło?")))])
# print(password)
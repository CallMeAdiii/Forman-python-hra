
global hp, xp, money
hp = 100
xp = 0
money =100

def add_hp(amount):
    global hp
    hp += amount
    if hp > 100:
        hp = 100

def add_hp2(amount):
    global hp
    if hp+amount > 100:
        hp = 100
    else:
        hp += amount
def stats():
    print(f"### HP {hp} ### XP {xp} ### {money} ###")

def welcome_screen():
    print("########################")
    print("     Vítej v RPG hře    ")
    print("########################")

    print("\nMenu:")
    print("1 - Zahájit hru")
    print("Cokoliv jiného - ukončit hru")

def tavern():
    global hp,money
    print("-----------------------")
    print("      Jsi v krčmě      ")
    print("-----------------------")

    stats()

    print("\nMenu:")
    print("1 - Koupím si pivo")
    print("2 - Koupím si polévku")
    print("3 - Koupím si velké jídlo")

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        if money < 20:
            print("Nemáš dostatek peněz")
        else:
            print("Koupil jsis báječné pivo")
        money -= 20
        hp += 5

    elif int(choice) == 2:
        if money <30:
            print("Nemáš dost peněz")
        else:print("Koupil jsis hnusnou polévku")
        money -= 30
        hp += 6

    elif int(choice) == 3:
        if money <50:
           print("Nemáš dost peněz")
        else:print("Dostal jsi před sebe půlku divočáka")
        money -= 50
        hp += 50

    stats()
    crossroad()

def crossroad():
    print("-----------------------")
    print("   Jsi na křizovatce   ")
    print("-----------------------")

    print("\nMenu:")
    print("1 - Tréninkové hriště")
    print("2 - Krčma")
    print("3 - Souboj")

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        print("Budeš trénovat")
    elif int(choice) == 2:
        tavern()
    elif int(choice) == 3:
        print("Budeš bojovat")
    else:
        crossroad()


def main():
    welcome_screen()

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        crossroad()
    else:
        print("Hra ukončena")


main()


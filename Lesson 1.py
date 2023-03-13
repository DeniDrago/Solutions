from copy import copy
from random import randint

warrior = {'name': 'Warrior', 'dmg': 20, 'hp': 100}
mage = {'name': 'Mage', 'dmg': 50, 'hp': 50}
archer = {'name': 'Archer', 'dmg': 40, 'hp': 70}


# character creation
def create_character():
    player1_charac = []
    player2_charac = []

    for name in range(2):
        player1_char = input("Player 1, choose your character (Warrior, Mage, or Archer): ")
        while player1_char.title() not in ['Warrior', 'Mage', 'Archer']:
            player1_char = input("Invalid choice.\nPlayer 1, choose your character (Warrior, Mage, or Archer): ")
        if player1_char.title() == 'Warrior':
            player1_charac.append(copy(warrior))
        elif player1_char.title() == 'Mage':
            player1_charac.append(copy(mage))
        else:
            player1_charac.append(copy(archer))

    for name in range(2):
        player2_char = input("Player 2, choose your character (Warrior, Mage, or Archer): ")
        while player2_char.title() not in ['Warrior', 'Mage', 'Archer']:
            player2_char = input("Invalid choice.\nPlayer 2, choose your character (Warrior, Mage, or Archer): ")
        if player2_char.title() == 'Warrior':
            player2_charac.append(copy(warrior))
        elif player2_char.title() == 'Mage':
            player2_charac.append(copy(mage))
        else:
            player2_charac.append(copy(archer))

    return player1_charac, player2_charac


# determining damage depending on the character
def calculate_damage(attacker, defender):
    if attacker["name"] == "Warrior" and defender["name"] == "Mage":
        return attacker['dmg'] * 1.5
    elif attacker["name"] == "Mage" and defender["name"] == "Archer":
        return attacker['dmg'] * 1.5
    elif attacker["name"] == "Archer" and defender["name"] == "Warrior":
        return attacker['dmg'] * 1.5
    else:
        return attacker['dmg']


# winner's health update
def update_hp(attacker):
    if attacker["name"] == "Warrior":
        attacker["hp"] = copy(warrior)["hp"]
    elif attacker["name"] == "Mage":
        attacker["hp"] = copy(mage)["hp"]
    else:
        attacker["hp"] = copy(archer)["hp"]


# randomly determine the first attacker
def first_attacker():
    return randint(1, 2)


# fight function
def start_battle(player1_char, player2_char):
    player1_current_character = 0
    player2_current_character = 0
    player1_attacker = first_attacker()    # randomly determine the first attacker

    while player1_current_character < len(player1_char) and player2_current_character < len(player2_char):
        if player1_attacker == 1:
            attacker = player1_char[player1_current_character]
            defender = player2_char[player2_current_character]
        else:
            attacker = player2_char[player2_current_character]
            defender = player1_char[player1_current_character]

        print(f"\n{attacker['name']} ({attacker['hp']} HP) attacks {defender['name']} ({defender['hp']} HP)")
        damage = int(calculate_damage(attacker, defender))  # determining damage depending on the character
        defender["hp"] = int(max(0, defender["hp"] - damage))
        print(f"\n{attacker['name']} deals ({damage} damage) to {defender['name']}")

        if defender['hp'] == 0:
            print(f"\n{defender['name']} has been defeated!")
            if player1_attacker == 1:
                player2_current_character += 1
            else:
                player1_current_character += 1
            update_hp(attacker)    # winner's health update
        else:
            if player1_attacker == 1:
                player1_attacker = 2
            else:
                player1_attacker = 1

    if player1_current_character == len(player1_char):
        print("\nPlayer 2 wins!")
    else:
        print("\nPlayer 1 wins!")


print("Welcome to the RPG game!", '\n')
player1_characters, player2_characters = create_character()    # character creation
start_battle(player1_characters, player2_characters)

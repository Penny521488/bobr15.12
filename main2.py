from Vampyre import Vampyre
from berserk import Berserk
from character import Character

# Назначаем Volodya вампиром
player1 = Character("Toose", 185, 50, 5)
player2 = Vampyre("Volodya", 200, 30, 30)  # Volodya теперь вампир
player3 = Berserk("Bulka barabulka", 300, 50, 1)

player1.print_stats()
player2.print_stats()
player3.print_stats()

def battle(player1, player2):
    while player1.health > 0 and player2.health > 0:
        player1.attack(player2)
        if player2.health == 0:
            print(f"{player2.name} програв раунд, {player1.name} виграє!")
            break
        player2.attack(player1)
        if player1.health == 0:
            print(f"{player1.name} програв раунд, {player2.name} виграє!")
            break

battle(player1, player2)
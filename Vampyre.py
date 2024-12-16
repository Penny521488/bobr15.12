
from character import Character

class Vampyre(Character):
    def __init__(self, name, health=100, damage=10, defence=5):
        super().__init__(name, health, damage, defence)

    def attack(self, target):
        # Вампир атакует цель
        print(f"{self.name} атакует {target.name} и высасывает жизнь!")
        target.take_damage(self.damage)


        heal_amount = int(self.damage * 0.1)
        self.health = min(self.health + heal_amount, 100)
        print(f"{self.name} восстанавливает {heal_amount} здоровья, текущее здоровье: {self.health}.")
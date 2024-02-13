from weapon import fists

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists
        
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        # Prevents health value going below zero
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} using (a) {self.weapon.name}")
        
class Hero(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        
        self.default_weapon  = self.weapon
        
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")
        
    def drop(self) -> None:
        if self.weapon.name is not "Fists":
            print(f"{self.name} dropped the {self.weapon.name}!")
            self.weapon = self.default_weapon
        else: print("The Hero cannot drop their fists!")

class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: str):
        super().__init__(name, health)
        self.weapon = weapon
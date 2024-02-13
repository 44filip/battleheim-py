from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy", health = 100, weapon = short_bow)
# The enemy will have a Short Bow as default, although it can be dropped

while hero.health > 0 and enemy.health > 0:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    
    hero.drop()
    enemy.drop()
    input()
    
if hero.health > enemy.health:
    print("The Hero wins!")
elif hero.health == enemy.health:
    print("It's a draw!")
else:
    print("The Enemy wins!")
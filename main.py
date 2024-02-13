from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy", health = 100, weapon = short_bow)
# The enemy will have a Short Bow as default, although it can be dropped
enemy_weapon_dropped = False

while hero.health > 0 and enemy.health > 0:
    hero.attack(enemy)
    enemy.attack(hero)
    
    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    if not enemy_weapon_dropped:
        enemy.drop()
        enemy_weapon_dropped = True
    input()
    
if hero.health > enemy.health:
    print("The Hero wins!")
elif hero.health == enemy.health:
    print("It's a draw!")
else:
    print("The Enemy wins!")
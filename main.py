from character import Hero, Enemy

hero = Hero(name = "Hero", health = 100)
enemy = Enemy(name = "Enemy", health = 100)

while hero.health > 0 and enemy.health > 0:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    
    input()
    
if hero.health > enemy.health:
    print("The Hero wins!")
elif hero.health == enemy.health:
    print("It's a draw!")
else:
    print("The Enemy wins!")
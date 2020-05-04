from classes.game import Person, BColors

magic = [
    {
        "name": "fire",
        "cost": 10,
        "dmg": 60,
    },
    {
        "name": "thunder",
        "cost": 10,
        "dmg": 60,
    },
    {
        "name": "wove",
        "cost": 10,
        "dmg": 60,
    },

]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

run = True
print(BColors.FAIL + BColors.BOLD + "AN ATTACKS !!!!" + BColors.ENDC)

while run:
    print("=============================")
    player.choose_action()
    index = int(input("Choose action : ")) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attack for ", dmg, " points of damage .\n Enemy HP is : ", enemy.hp)



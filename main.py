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

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))

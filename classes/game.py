import random


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNINIG = '\033[933m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.action = ["attack", "magic"]

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def generate_spell_damage(self, index):
        return random.randrange(self.magic[index]["dmg"] - 5, self.magic[index]["dmg"] + 5)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def set_reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, index):
        return self.magic[index]["name"]

    def get_spell_cost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        index = 1
        print("action : ")
        for item in self.action:
            print(str(index) + " : ", item)
            index += 1

    def choose_magic(self):
        print("magic : ")
        index = 1
        for item in self.magic:
            print(str(index) + " : ", item["name"], "(cost : ", str(item["mp"]) + ")")
            index += 1

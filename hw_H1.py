import random

class Warrior:
    def __init__(self, name = None, hp=None):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f'На поле выходит: {self.name}, HP: {self.hp}'

class Zombie(Warrior):
    def __init__(self, name = None, hp=None):
        super().__init__(name, hp)

class Survivor(Warrior):
    def __init__(self, name = None, hp=None):
        super().__init__(name, hp)


z = Zombie('Zerg',100)
s = Survivor('John', 100)
print(z)
print(s)

while True:
    a = random.randint(0,1)
    s_attack = random.randint(0,20)
    z_attack = random.randint(0,20)
    if a == 0:
        z.hp = z.hp - s_attack
        if s_attack <= 16:
            print(f'{s.name} атакует и отнимает {s_attack} жизней у противника ')
        else:
            print(f'{s.name} наносит критический урон и отнимает {s_attack} жизней у противника')
    elif a== 1:
        s.hp = s.hp - z_attack
        if z_attack <= 16:
            print(f'{z.name} атакует и отнимает {z_attack} жизней у противника ')
        else:
            print(f'{z.name} наносит критический урон и отнимает {z_attack} жизней у противника')
    if s.hp <= 0:
        print(f'{z.name} победил!')
        break
    if z.hp <= 0:
        print(f'{s.name} победил!')
        break
from textwrap import dedent

from ex45_dice_roll import *
from ex45_artefacts import *
import random


class Person(object):

    def __init__(self, name, hp, melee, distant, knowledge):
        self.name = name
        self.hp = hp
        self.melee = melee
        self.distant = distant
        self.knowledge = knowledge

    def get_hp(self):
        return self.hp

    def get_melee(self):
        return self.melee

    def get_distant(self):
        return self.distant

    def get_knowledge(self):
        return self.knowledge

    def isAlive(self):
        if self.hp > 0:
            return True
        elif self.hp <= 0:
            return False
        else:
            exit(0)

    def print_abilities(self):
        print("_______________________________")
        print(f"""
            Очки жизни: {self.hp}
            Урон в ближнем бою: {self.melee}
        """)

    def change_abilities(self, ability, value):
        if ability == 'hp':
            self.hp += value
            print(f"Очки жизни {self.name} изменились на {value}")
        elif ability == 'melee':
            self.melee += value
            print(f"Ваш урон в ближнем бою изменился на {value}")
        elif ability == 'distant':
            self.distant += value
            print(f"Ваш урон в дальнем бою изменился на {value}")
        elif ability == 'knowledge':
            self.knowledge += value
            print(f"Ваш уровень знаний изменился на {value}")
        else:
            exit(1)

    def register_hit(self, damage):
        self.change_abilities('hp', -damage)

    def show_ability(self, ability):
        if ability == 'melee':
            return self.melee
        elif ability == 'distant':
            return self.distant
        elif ability == 'knowledge':
            return self.knowledge
        else:
            exit(0)

    def damage_melee(self):
        print(f"Вам нанесен урон {self.show_ability('melee')}")
        return self.show_ability('melee')


class Hero(Person):

    def print_abilities(self):
        super().print_abilities()
        print(f"""
            Урон дальнего боя: {self.distant}
            Уровень знаний: {self.knowledge}
        """)
        print("_______________________________")

    def damage_melee(self):
        ability = self.show_ability('melee')
        damage = ability + roll()
        print(f"Вами нанесен урон {damage}")
        return damage

    def damage_distant(self):
        ability = self.show_ability('distant')
        damage = ability + roll()
        print(f"Вами нанесен урон {damage}")
        return damage

    def be_clever(self):
        ability = self.show_ability('knowledge')
        damage = ability + roll()
        print(f"Ваши знания сегодня на уровне {damage}")
        return damage

    def choose_ability(self):
        print("_______________________________")
        print(f"""
        Пожалуйства выберите вид урона:
        1. Урон в ближнем бою - {self.melee} + кубик
        2. Урон в дальнем бою - {self.distant} + кубик
        """)

        choice = input("Ведите цифру: ")
        if choice == '1':
            return self.damage_melee()
        elif choice == '2':
            return self.damage_distant()
        else:
            print("Введите одно из следующих значений:")
            return self.choose_ability()

    def get_defend_artefact(self):
        print(f"""
            Поздравляю этот артефакт - {random.choice(items_defend)} {random.choice(description_defend)} {random.choice(title_defend)}
        """)
        self.change_abilities('hp', random.randint(1, 20))
        self.change_abilities('knowledge', random.randint(0, 5))

    def get_attack_artefact(self):
        print(f"""
            Поздравляю этот артефакт - {random.choice(items_attack)} {random.choice(description_attack)} {random.choice(title_attack)}
        """)
        self.change_abilities('melee', random.randint(1, 10))
        self.change_abilities('distant', random.randint(0, 7))

    def choose_sort_of_artefact(self):
        print(dedent("""
            _______________________________
            Вы победили врага и с него выпал артефакт
            Пожалуйста выберите какой артефакт вы хотите получить:
            (От этого зависят ваши характеристики)
            1. Атакующий
            2. Защитный
        """))
        choice = input("Пожалуйста введите цифру >")
        if choice == '1':
            self.get_attack_artefact()
        elif choice == '2':
            self.get_defend_artefact()
        else:
            print("Пожалуйста введите одну цифру")
            return self.choose_sort_of_artefact()


class Enemy(Person):
    pass

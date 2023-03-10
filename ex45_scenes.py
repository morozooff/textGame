from sys import exit
from random import randint
import random
from textwrap import dedent

from ex45_persons import *
from ex45_persons import Hero


class Scene(object):

    def enter(self):
        print("Эта сцена еще не настроена.")
        print("Создайте подкласс и реализуйте функцию enter().")
        exit(1)

    ivan = Hero('Иван', 20, 5, 4, 4)
    goblin = Enemy('Антон', 8, 3, 0, 0)
    troll = Enemy('Игорь', 13, 6, 0, 0)
    snake = Enemy('Василий', 10, 9, 0, 0)
    dragon = Enemy('Алексей', 25, 10, 0, 0)


class Engine(Scene):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        last_scene = self.scene_map.next_scene('victory')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Start(Scene):
    def enter(self):
        print(dedent("""
            Пожалуйста выберите уровень сложности
            1. Легкий
            2. Средний
            3. Невероятно сложный
        """))
        choice = input("Введите цифру, соответствующую уровню сложности >")
        if choice == '1':
            self.ivan.change_abilities('hp', 5)
            self.ivan.change_abilities('melee', 1)
            self.ivan.change_abilities('distant', 1)
            self.ivan.change_abilities('knowledge', 1)
            self.goblin.change_abilities('hp', -1)
            self.troll.change_abilities('hp', -1)
            self.troll.change_abilities('melee', -1)
            self.snake.change_abilities('hp', -2)
            self.dragon.change_abilities('hp', -5)
            self.dragon.change_abilities('melee', -2)
        elif choice == '2':
            pass
        elif choice == '3':
            self.ivan.change_abilities('hp', -3)
            self.ivan.change_abilities('melee', -1)
            self.ivan.change_abilities('distant', -1)
            self.ivan.change_abilities('knowledge', -2)
            self.goblin.change_abilities('hp', 1)
            self.goblin.change_abilities('melee', 1)
            self.troll.change_abilities('hp', 1)
            self.troll.change_abilities('melee', 1)
            self.snake.change_abilities('hp', 1)
            self.snake.change_abilities('melee', 2)
            self.dragon.change_abilities('hp', 5)
            self.dragon.change_abilities('melee', 2)
        else:
            print("Пожалуйста введите одну цифру")
            return self.enter()
        return 'cave'


class Death(Scene):
    quips = [
        "Умер",
        "Потрачено",
        "Пал смертью храбрых"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class Cave(Start):

    def enter(self):
        print("_______________________")
        print(dedent(f"""
            Вы в начале игры
            Ваш герой Иван стоит перед входом в пещеру
            Его характеристики:
            """))
        self.ivan.print_abilities()

        print(dedent("""
            Приготовьтесь, в пещере вас ждет множество опасностей и приключений
            Вам предстоит сразиться с врагами и разгадать загадку
        """))

        input("Нажмите enter, чтобы зайти в пещеру")
        print("Вы зашли в пещеру...")
        return 'cave_entry'


class CaveEntry(Start):
    def enter(self):
        print("_______________________")
        victory = False
        print(dedent(f"""
                В первой же комнате вас встречает злой Гоблин {self.goblin.name}.
                Он выглядит агрессивно и, только завидев вас, 
                без объяснений бросается в атаку.
                Впереди трудный бой, готовтесь!
                
                Его характеристики:
                """))

        while True:
            self.goblin.print_abilities()
            print("Вы атакуете: ")
            damage = self.ivan.choose_ability()
            self.goblin.register_hit(damage)

            if not self.goblin.isAlive():
                victory = True
                print(f"{self.goblin.name} умер, вы победили")
                break
            else:
                pass

            print("Атакует Гоблин: ")
            goblin_damage = self.goblin.show_ability('melee')
            print(f"{self.goblin.name} наносит {goblin_damage} урона")
            self.ivan.register_hit(goblin_damage)
            print(f"Теперь ваши очки жизни равны {self.ivan.hp}")

            if not self.ivan.isAlive():
                break
            else:
                pass

        if victory:
            self.ivan.choose_sort_of_artefact()
            return 'fork'
        else:
            return 'death'


class Fork(Start):
    def enter(self):
        print(dedent("""
                             Вы на развилке и можете пройти дальше, 
                             перед вами две двери:
                             1. Комната Страха
                             2. Комната Ужаса
                             В какую вы войдете?
                             Пожалуйста введите номер комнаты:
                            """))
        choice = input()
        if choice == '1':
            self.ivan.print_abilities()
            return 'fear_room'
        elif choice == '2':
            return 'horror_room'
        else:
            print(dedent("Пожалуйства введите цифру, обозначающую одно из действий"))
            return self.enter()


class FearRoom(Start):
    def enter(self):
        print("_______________________")
        victory = False
        print(dedent(f"""
            Вы входите в комнату Страха и там находится
            огромный жирный Тролль {self.troll.name}.
            Чтобы пройти дальше вам придется сразиться с ним
            
            Его характеристики:
            """))

        while True:
            self.troll.print_abilities()
            print("Вы атакуете: ")
            damage = self.ivan.choose_ability()
            self.troll.register_hit(damage)

            if not self.troll.isAlive():
                victory = True
                print(f"{self.troll.name} умер, вы победили")
                break
            else:
                pass

            print(f"Атакует {self.troll.name}: ")
            troll_damage = self.troll.show_ability('melee')
            print(f"{self.troll.name} наносит {troll_damage} урона")
            self.ivan.register_hit(troll_damage)
            print(f"Теперь ваши очки жизни равны {self.ivan.hp}")

            if not self.ivan.isAlive():
                break
            else:
                pass

        if victory:
            self.ivan.choose_sort_of_artefact()
            self.fear_passed_change()
            return 'mystery_room'
        else:
            return 'death'


class HorrorRoom(Start):
    def enter(self):
        print("_______________________")
        victory = False
        print(dedent(f"""
                    Вы входите в комнату Ужаса и там находится
                    ядовитый Змей {self.snake.name}.
                    Чтобы пройти дальше вам придется сразиться с ним
    
                    Его характеристики:
                    """))

        while True:
            self.snake.print_abilities()
            print("Вы атакуете: ")
            damage = self.ivan.choose_ability()
            self.snake.register_hit(damage)

            if not self.snake.isAlive():
                victory = True
                print(f"{self.snake.name} умер, вы победили")
                break
            else:
                pass

            print(f"Атакует {self.snake.name}: ")
            snake_damage = self.snake.show_ability('melee')
            print(f"{self.snake.name} наносит {snake_damage} урона")
            self.ivan.register_hit(snake_damage)
            print(f"Теперь ваши очки жизни равны {self.ivan.hp}")

            if not self.ivan.isAlive():
                break
            else:
                pass

        if victory:
            self.ivan.choose_sort_of_artefact()
            return 'mystery_room'
        else:
            return 'death'


class MysteryRoom(Start):
    def enter(self):
        print(dedent("""
            Вы находитесь в загадочной комнате
            Постепенно обойдя всю комнату вы набредаете на дверь
            На ней висит замок
            Вы понимаете, для того, чтобы открыть дверь вам
            нужно ввести три цифры 
            
            На стенах вы видите письмена, быть может вашего уровня знаний
            хватит для того, чтобы их прочитать
            
        """))
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        third = random.randint(0, 9)
        code = str(first) + str(second) + str(third)
        check = input("Пожалуйста нажмите enter, чтобы прочитать")
        if check == 'mellon':
            print(code)
        else:
            pass

        print("Вы читаете...")
        isGuessed = False
        time.sleep(2)

        if self.ivan.knowledge >= 5:
            print(dedent(f"""
                  Вы явно что-то знаете, теперь вам известны
                  первые две цифры пароля - {str(first) + str(second)}
                  Осталось подобрать последнюю:
                  Введите цифру
                  """))
            for i in range(0, 9):
                attempt = input(">")
                if attempt == str(third):
                    isGuessed = True
                    break
                else:
                    continue
        else:
            print("К сожалению, иероглифы не поддаются осмыслению")
            print("Вам придется угадывать все три цифры")
            for i in range(0, 9):
                attempt = input(">")
                if attempt == code:
                    isGuessed = True
                    break
                else:
                    continue

        if isGuessed:
            print(dedent("Поздравляю вы нашли правильный код и можете пройти дальше"))
            return 'boss_room'
        else:
            print(dedent("""
                        После девятой попытки стены в этой комнате
                        начинают издавать странные звуки
                        Непримечательные шлюзы на них открываются, двери закрываются
                        и комната начинает заполняться
                        
                        Вам ничего не остается делать как умирать))))
                        """))
            return 'death'


class BossRoom(Start):
    def enter(self):
        print("_______________________")
        victory = False
        print("Войдя в дверь вы осматриваетесь...")
        time.sleep(2)
        print("В комнате лежат горы золота")
        time.sleep(2)
        print("Вы берете одну из понравившихся монет, чтобы осмотреть...")
        time.sleep(2)
        print("Вдруг золото по всей комнате начинает сыпаться..")
        time.sleep(2)
        print("Что-то или кто-то просыпается..")
        time.sleep(2)

        print(dedent(f"""
                    Это ДРАКОН {self.dragon.name}!!!!!!!!!!
                    Чтобы пройти дальше вам придется сразиться с ним

                    Его характеристики:
                    """))

        while True:
            self.dragon.print_abilities()
            print("Вы атакуете: ")
            damage = self.ivan.choose_ability()
            self.dragon.register_hit(damage)

            if not self.dragon.isAlive():
                victory = True
                print(f"{self.dragon.name} умер, вы победили")
                break
            else:
                pass

            print(f"Атакует {self.dragon.name}: ")
            dragon_damage = self.dragon.show_ability('melee')
            print(f"{self.dragon.name} наносит {dragon_damage} урона")
            self.ivan.register_hit(dragon_damage)
            print(f"Теперь ваши очки жизни равны {self.ivan.hp}")

            if not self.ivan.isAlive():
                break
            else:
                pass

        if victory:
            self.ivan.choose_sort_of_artefact()
            return 'victory'
        else:
            return 'death'


class Victory(Start):
    def enter(self):
        print(dedent(f"""
        Дракон побежден!
        Вы радуетесь и собираетесь забрать все сокровища
        Набив полные сумки вы видите, что из пещеры ведут три двери
        
        На первой написано:
        "Будешь непобедим"
        
        Вторая гласит:
        "Будешь силен"
        
        Третья:
        "Великое знание обретешь"
        
        Какую дверь ты выберешь?
        1. "Будешь непобедим"
        2. "Будешь силен"
        3. "Великое знание обретешь"
        """))
        choice = input("Введите номер двери >")
        if choice == '1':
            self.ivan.change_abilities('hp', 1000)
            self.ivan.print_abilities()
            print(dedent("""
            Вы заходите в дверь и чувствуете как ваше тело крепнет
            
            Выйдя из пещеры вы понимаете, что теперь равных вам в мире нет
            Вас не берет ни одна болезнь
            Своим трудолюбием и жизнелюбием вы делитесь с окружающими
            Вас любят и уважают
            Вы проживаете долгую и счасливую жизнь, совершая еще не одну победу
            Но это приключение вам запомнится по-особенному...
            """))
        elif choice == '2':
            self.ivan.change_abilities('melee', 500)
            self.ivan.change_abilities('distant', 500)
            self.ivan.print_abilities()
            print(dedent("""
                        Вы заходите в дверь и чувствуете невероятный прилив сил

                        Выйдя из пещеры вы понимаете, что теперь равных вам в мире нет
                        Вы становитесь самым дорогим наемником, таким, который в одиночку 
                        может решать судьбы сражений и сложных заданий
                        Слава о ваших деяниях и победах проходит сквозь века
                        Вы проживаете веселую и счасливую жизнь, совершая еще не одну победу
                        Но это приключение вам запомнится по-особенному...
                        """))
        elif choice == '3':
            self.ivan.change_abilities('knowledge', 1000)
            self.ivan.print_abilities()
            print(dedent("""
                                    Вы заходите в дверь и чувствуете как самые разные мысли лезут в вашу голову

                                    Выйдя из пещеры вы понимаете, что теперь равных вам в мире нет
                                    Вы совершаете самые важные открытия за всю историю человечества
                                    Своими открытиями и изобретениями вы помогаете решить множество проблем
                                    К вам ходят за советом и крестьяне и короли
                                    Ваше имя навсегда останется в истории
                                    Вы проживаете осмысленную и счасливую жизнь, совершая еще не одну победу
                                    Но это приключение вам запомнится по-особенному...
                                    """))
        else:
            return self.enter()


class Map(object):
    scenes = {
        'start': Start(),
        'cave': Cave(),
        'cave_entry': CaveEntry(),
        'fork': Fork(),
        'fear_room': FearRoom(),
        'horror_room': HorrorRoom(),
        'mystery_room': MysteryRoom(),
        'boss_room': BossRoom(),
        'death': Death(),
        'victory': Victory()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('start')
a_game = Engine(a_map)
a_game.play()


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print("имя:", self.name)
        print("возраст:", self.age)


class Level:
    def __init__(self, number):
        self.number = number
        self.humans = []

    def add_human(self, human):
        self.humans.append(human)

    def get_info(self):
        print("уровень:", self.number)
        if self.humans:
            print("люди на этом уровне:")
            for h in self.humans:
                h.get_info()
        else:
            print("на этом уровне больше нет людей")


class Platform:
    def __init__(self, resources):
        self.resources = resources
        self.food = 0

    def add_food(self, amount):
        self.food += amount
        print("Добавлено еды:", amount)
        print("всего еды:", self.food)

    def subtract_resources_for_people(self, levels, cost_per_person):
        for level in levels:
            alive = []
            for human in level.humans:
                if self.resources >= cost_per_person:
                    self.resources -= cost_per_person
                    alive.append(human)
                else:
                    print(human.name, "умер (не хватило ресурсов)")
            level.humans = alive
        print("осталось ресурсов:", self.resources)

    def subtract_food_for_people(self, levels, food_per_person):
        for level in levels:
            alive = []
            for human in level.humans:
                if self.food >= food_per_person:
                    self.food -= food_per_person
                    alive.append(human)
                else:
                    print(human.name, "умер (не хватило еды)")
            level.humans = alive
        print("осталось еды:", self.food)


h1 = Human("Mati", 25)
h2 = Human("Kati", 30)

level1 = Level(1)
level2 = Level(2)

level1.add_human(h1)
level2.add_human(h2)

platform = Platform(50)
platform.add_food(60)

level1.get_info()
level2.get_info()

platform.subtract_resources_for_people([level1, level2], 2)
platform.subtract_food_for_people([level1, level2], 5)

level1.get_info()
level2.get_info()
    

class Toy:

    def __init__(self, name ="SomeName", sex ="SomeSex", composition ="Unknow"):
        print(f" __INIT__Toy {name}, {sex}")
        self.name = name
        self.sex = sex
        self.composition = composition


    def info(self):
        print(f" INFO Toy {self.name} {self.sex}")
        return f"Name: {self.name}, Sex: {self.sex}, composition: {self.composition}"

    def say(self):
        return "woof"

class Cat(Toy):
    def say(self):
        return "Meow"

a = Cat("Zevs", "Boy", "Wool")

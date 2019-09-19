import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
    def attack(self):
        print(random.randint(0,self.max_damage))


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
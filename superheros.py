import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
    def attack(self):
        attack_value = random.randint(0,self.max_damage)
        return attack_value

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block_value = random.randint(0,self.max_block)
        return block_value


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.health = starting_health

    def current_health(self):
        health_value = int(self.health)
        return health_value

    def add_ability(self, ability):
        pass

        

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
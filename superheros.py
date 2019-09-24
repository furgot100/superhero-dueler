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
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities= []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        
        self.attack_power = 0

    # def current_health(self):
    #     return self.starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)


    # def abilities(self):
    #     return self.ability_list

    def attack(self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total

    def add_armor(self,armor):
        self.armors.append(armor)
    
    def defend(self):
        total = 0 
        for armor in self.armors:
            total += armor.block()
        return total

    def take_damage(self,damage):
        self.current_health -= (damage - self.defend())
        


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    # print(ability.name)
    # print(ability.attack())
   
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    my_hero = Hero("Grace Hopper", 200)
    my_hero.add_ability(ability)
    my_hero.add_ability(another_ability)
    print(my_hero.attack())
    
    # print(my_hero.name)
    # print(my_hero.current_health())
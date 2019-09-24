from random import randint
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

class Weapon(Ability):
    def attack(self):
        return randint(self.max_damage // 2 , self.max_damage)

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

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
        
    def fight(self,opponent):
        if self.abilities != [] and opponent.abilities != []:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                print(f"{opponent.name} has {opponent.current_health} health.")
                self.take_damage(opponent.attack())
                print(f"{self.name} has {self.current_health} health.")
            if self.is_alive():
                print(f"{self.name} wins!")
            else:
                print(f"{opponent.name} wins!")
        else:
            print("Draw!")    

class Team():
    def __init__(self,name):
        self.name = name 
        self.heroes = []

    def remove_hero(self,name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return 
        return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    # print(ability.name)
    # print(ability.attack())
   
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    
    # print(my_hero.name)
    # print(my_hero.current_health())
from random import randint,choice
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
        self.deaths = 0 
        self.kills = 0

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
                self.add_kill(1)
                opponent.add_deaths(1)
            else:
                print(f"{opponent.name} wins!")
                self.add_deaths(1)
                opponent.add_kill(1)
        else:
            print("Draw!")    

    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        self.deaths =+ num_deaths
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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

    def add_hero(self,hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        fighting = True
        team_one = []
        team_two = []

        while fighting:
            team_one.clear()
            team_two.clear()
            for hero in self.heroes:
                if hero.is_alive():
                    team_one.append(hero)
            for hero in other_team.heroes:
                if hero.is_alive():
                    team_two.append(hero)
            if len(team_one) <= 0 or len(team_two) <= 0:
                fighting = False
            else:
                hero_one = choice(team_one)
                hero_two = choice(team_two)
                hero_one.fight(hero_two)

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = hero.starting_health
    
    def stats(self):
        print(f"Name | Kill / Death")
        for hero in self.heroes:
            print(f"{hero.name} | {hero.kills} / {hero.deaths}")

class Arena():
    def __init__(self):
        self.team_one = []
        self.team_two = []

    def create_ability(self):
        new_ability = input('Enter a new ability: ')
        max_damage = int(input("Enter Maximum damage: "))
        ability = Ability(new_ability, max_damage)
        return ability

    def create_weapon(self):
        new_weapon = input("Enter a new weapon: ")
        damage = int(input("Enter damage: "))
        weapon = Weapon(new_weapon,damage)
        return weapon

    def create_armor(self):
        new_armor = input("Enter new armor name: ")
        block_stat = int(input("Enter block number: "))
        armor = Armor(new_armor, block_stat)
        return armor

    def create_hero(self):
        name = input("Enter name of Hero: ")
        health = int(input("Enter starting health of your Hero: "))
        hero = Hero(name, health)
        
        user_ability = input("Does your Hero have abilities?(y/n): ")
        while user_ability.isalpha == False:
            user_ability = input("Does your Hero have abilities?(y/n): ")

        user_weapon = input("Does your Hero have weapons?(y/n): ")
        while user_ability.isalpha() == False:
            user_weapon = input("Does your Hero have weapons?(y/n): ")

        user_armor = input("Does your Hero have armor?(y/n): ")
        while user_armor.isalpha() == False:
            user_armor = input("Does your Hero have armor?(y/n): ")

        if user_ability == "y":
            hero.add_ability(self.create_ability())
        if user_weapon == "y":
            hero.add_ability(self.create_weapon())
        if user_armor == "y":
            hero.add_armor(self.create_armor)

        #Shoutout to Jeric for helping me make my code neater

        return hero

    def build_team_one(self):
        user_input = input("What's the name of team one? ")
        team_one = user_input
        num_hero = int(input("How many memebers?: "))
        for i in range(num_hero):
            hero = self.create_hero()
            team_one.add_hero(hero)
        self.team_one = team_one   
    def build_team_two(self):
        user_input = input("What's the name of team two? ")
        team_two = user_input
        num_hero = int(input("How many heroes?: "))
        for i in range(num_hero):
            hero = self.create_hero()
            team_two.add_hero(hero)
        self.team_two = team_two
    
    def dead_team(self,team_alive):
        team_deaths = 0
        for hero in team_alive:
            if hero.current_health == 0:
                team_deaths += 1
        if team_deaths == len(team_alive):
            return True
        else:
            return False

    def team_battle(self):
        self.team_one.attack(self.team_two)


    def show_stats(self):
        team_one = self.team_dead(self.team_one.heroes)
        team_two = self.team_dead(self.team_two.heroes)

        if team_one == False:
            print(f"Team {self.team_one.name} wins!")
            print("Heroes remaning: ")
            for hero in self.team_one.heroes:
                if hero.is_alive():
                    print(hero.name)
        elif team_two == False:
            print(f"Team {self.team_two.name} wins!")
            print("Heroes remaining: ")
            for hero in self.team_one.heroes:
                if hero.is_alive():
                    print(hero.name)
                else:
                    print("They're all dead!")
        elif team_one == False and team_two == False:
            print("Draw!")

        print(f"Team one KDR: {self.team_one.stats()}")  
        print(f"Team two KDR: {self.team_two.stats()}")

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
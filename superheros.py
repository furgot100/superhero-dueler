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
        return randint(0,self.max_block)

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
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def defend(self):
        total_def = 0 
        for hero in self.armors:
            total += hero.block()
        return total_def

    def take_damage(self,damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
        
    def fight(self,opponent):
        # if self.abilities != [] and opponent.abilities != []:
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)
            opponent.take_damage(hero_attack)
        if self.is_alive() == False and opponent.is_alive() == False:
            print("Draw!")
        elif opponent.is_alive() == False:
            print(f'{self.name} won')
            self.add_kill(1)
            opponent.add_deaths(1)
        elif self.is_alive() == False:
            print(f'{opponent.name} won')
            opponent.add_kill(1)
            self.add_deaths(1) 

    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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
        all_heroes = []
        for hero in self.heroes:
            all_heroes.append(hero)
        print(all_heroes)

    def add_hero(self,hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        hero = self.heroes[random.randint(0,(len(self.heroes))-1)]
        hero_two = other_team.heroes[random.randint(0,(len(other_team.heroes))-1)]
        hero.fight(hero_two)

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
        return Ability(new_ability, max_damage)

    def create_weapon(self):
        new_weapon = input("Enter a new weapon: ")
        damage = int(input("Enter damage: "))
        return Weapon(new_weapon,damage)

    def create_armor(self):
        new_armor = input("Enter new armor name: ")
        block_stat = int(input("Enter block number: "))
        return Armor(new_armor, block_stat)

    def create_hero(self):
        name = input("Enter name of Hero: ")
        health = int(input("Enter starting health of your Hero: "))
        hero = Hero(name, health)
        
        user_ability = input("Does your Hero have abilities?(y/n): ")
        # while user_ability.isalpha == False:
        #     user_ability = input("Does your Hero have abilities?(y/n): ")

        user_weapon = input("Does your Hero have weapons?(y/n): ")
        # while user_ability.isalpha() == False:
        #     user_weapon = input("Does your Hero have weapons?(y/n): ")

        user_armor = input("Does your Hero have armor?(y/n): ")
        # while user_armor.isalpha() == False:
        #     user_armor = input("Does your Hero have armor?(y/n): ")

        if user_ability.lower() == "y":
            hero.add_ability(self.create_ability())
        if user_weapon.lower() == "y":
            hero.add_weapon(self.create_weapon())
        if user_armor.lower() == "y":
            hero.add_armor(self.create_armor())

        #Shoutout to Jeric for helping me make my code neater
        
        return hero

    def build_team_one(self):
        user_input = input("What's the name of team one? ")
        team_one = Team(user_input)
        num_hero = int(input("How many heroes?: "))
        # while num_hero.isnumeric == False:
        #     num_hero = input("How many heroes?: ")
        for index in range(num_hero):
            hero = self.create_hero()
            team_one.add_hero(hero)
        self.team_one = team_one
        
        # self.team_one = Team(team_one)
    def build_team_two(self):
        user_input = input("What's the name of team two? ")
        team_two = Team(user_input)
        num_hero = int(input("How many heroes?: "))
        
        
        for index in range(num_hero):
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
        team_one = self.dead_team(self.team_one.heroes)
        team_two = self.dead_team(self.team_two.heroes)

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
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
    
    
    
    
    
    
    
    
    # If you run this file from the terminal
    # this block is executed.
    # print(ability.name)
    # print(ability.attack())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    # print(my_hero.name)
    # print(my_hero.current_health())
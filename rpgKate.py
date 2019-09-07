"""
In this simple RPG game, the gyro fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character: 
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self):
        return self.health > 0
    def attack(self, enemy):
        enemy.health -= self.power 
        return "You do {} damage to the {}.".format(self.power, enemy.name)
    def print_status(self): 
        if self.health <= 0:
            return "You are dead."
        else: 
            return "You have {} health and {} power.".format(self.health, self.power)

class Hero(Character): 
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
class Goblin(Character): 
    def __init__(self, name, health, power):
        self.name = name 
        self.health = health
        self.power = power
       
     
goblin = Goblin("Goblin", 6, 2)
hero = Hero("Hero", 10, 5)
zombie = Character("Zombie", ,1)

def main():
   
    while goblin.alive() and hero.alive():
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            print(hero.attack(goblin))
        elif user_input == "2":
            pass
        elif user_input == "3":
            return "Goodbye."
            break
        else:
            return "Invalid input %r" % user_input
        if goblin.health > 0:
            print(goblin.attack(hero))
            print(hero.print_status)
        
main()

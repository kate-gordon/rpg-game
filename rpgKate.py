"""
In this simple RPG game, the gyro fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character: 
    def __init__(self, health, power)
        self.health = health
        self.power = power
    def alive(self):
        return self.health > 0
    def attack(self, enemy):
        enemy.health -= self.power 
        return "You do %s damage to the %s." % self.power, enemy.name

class Hero(Character): 
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def print_status(self): 
        if Hero.health <= 0:
            return "You are dead."
        else: 
            return "You have %d health and %d power." % (gyro.health, gyro.power)
        
class Goblin(Character): 
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name 

    def attack(Hero):
        gyro.health -= goblin.power
        return "The goblin does %d damage to you." % goblin.power

    def print_status(self):
        if goblin.health <= 0:
            return "The goblin is dead."
        else:
            return"The goblin has %d health and %d power." % (goblin.health, goblin.power)
     
goblin = Goblins("goblin1",6, 2)
gyro = Hero(10, 5)

def main():
   
    while goblin.alive() and gyro.alive():
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            gyro.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            return "Goodbye."
            break
        else:
            return "Invalid input %r" % user_input
        if goblin.health > 0:
         goblin.attack(gyro)
        
main()

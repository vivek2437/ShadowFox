# 8. Classes and Objects:
# 1.Avengers is a Marvel’s American Superheroes team, Now you want to
# showcase your programming skills by representing the Avengers team using
# classes. Create a class called Avenger and create these six superheroes using this
# class.
# 2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk",
# "Thor", "Hawkeye"]
# 3. Your Avenger class should have these properties:
# 1. Name
# 2. Age
# 3. Gender
# 4. Super Power
# 5. Weapon
# 4. Captain America has Super strength, Iron Man has Technology, Black Widow
# is superhuman, Hulk has Unlimited Strength, Thor has super Energy and
# Hawkeye has fighting skills as superpowers.
# 5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and
# Arrows
# 6. Create methods to get the information about each superhero
# 7. Create a method is_leader() which will tell if the superhero is a leader or not.
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Gender      : {self.gender}")
        print(f"Super Power : {self.super_power}")
        print(f"Weapon      : {self.weapon}")
        print()

    def is_leader(self):
        return self.name == "Captain America"


# Creating the list of Avengers
super_heroes = [
    Avenger("Captain America", 105, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")
]

# Display info and leader check
for hero in super_heroes:
    hero.get_info()
    if hero.is_leader():
        print(f"{hero.name} is the leader of the Avengers.")
    else:
        print(f"{hero.name} is not the leader.")
    print("-" * 40)

import random

class CharacterClass:
    WARRIOR = 0
    ROGUE = 1
    RANGER = 2
    MAGE = 3

class AttackType:
    STANDARD = 0
    RANGED = 1

class Character:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.level = 1
        self.experience = 0
        self.character_class = None
        self.attack_type = None

    def display_info(self):
        print("Name:", self.name)
        print("Class:", self.character_class)
        print("Attack Type:", self.attack_type)
        print("Health:", self.health)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Level:", self.level)
        print("Experience:", self.experience)
        print()

def create_character():
    character = Character()

    character.name = input("Enter character name: ")

    # Randomize character classes
    class_choice = random.randint(0, 3)
    if class_choice == 0:
        character.character_class = CharacterClass.WARRIOR
        character.attack_type = AttackType.STANDARD
    elif class_choice == 1:
        character.character_class = CharacterClass.ROGUE
        character.attack_type = AttackType.STANDARD
    elif class_choice == 2:
        character.character_class = CharacterClass.RANGER
        character.attack_type = AttackType.RANGED
    elif class_choice == 3:
        character.character_class = CharacterClass.MAGE
        character.attack_type = AttackType.RANGED

    random.seed()  # seed the random number generator

    character.health = random.randint(30, 40)
    character.defense = random.randint(8, 15)

    # set attack based on class
    if character.character_class in [CharacterClass.RANGER, CharacterClass.MAGE]:
        character.attack = random.randint(8, 12)
    else:
        # standard attack for warriors and rogues
        character.attack = random.randint(12, 18)

    return character

def ask_user_if_liked(character_name):
    response = input(f"Do you like the character {character_name}? (y/n): ")
    return response.lower() == 'y'

def display_character_details(character):
    print("Name:", character.name)
    print("Health:", character.health)
    print("Attack:", character.attack)
    print("Defense:", character.defense)
    print()

    # Display the character's class
    class_name = {
        CharacterClass.WARRIOR: "Warrior",
        CharacterClass.ROGUE: "Rogue",
        CharacterClass.RANGER: "Ranger",
        CharacterClass.MAGE: "Mage",
    }.get(character.character_class, "")

    print("Class:", class_name)
    print()

def main():
    characters = []

    for _ in range(3):
        new_character = Character()
        user_likes_character = False

        while not user_likes_character:
            new_character = create_character()
            display_character_details(new_character)
            user_likes_character = ask_user_if_liked(new_character.name)

        characters.append(new_character)

    print("All characters created:")
    for i, character in enumerate(characters, start=1):
        print(f"Character {i}:")
        print("Name:", character.name)
        print("Health:", character.health)
        print("Attack:", character.attack)
        print("Defense:", character.defense)
        print()

if __name__ == "__main__":
    main()

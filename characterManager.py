# Character creation stuff
class characterManager:
    def __init__(self):
        self.characters = {}

    def characterExists(self, name):
        if name in self.characters:
            return True
        return False

    def addCharacter(self, name, owner):
        # False for already exists True for successfully created character
        if self.characterExists(name):
            return False
        self.characters[name] = Character(name, owner, False)
        return True

    def setActive(self, name, owner):
        if self.characterExists(name) and self.characters[name].owner == owner:
            for character in self.characters:
                if self.characters[character].owner == owner:
                    self.characters[character].active = False
            self.characters[name].active = True
            return True
        else:
            return False

    def getCharacters(self, owner):
        ownersCharacters = []
        for character in self.characters:
            if self.characters[character].owner == owner:
                ownersCharacters.append(character)
        return ownersCharacters

    def getLanguages(self, characterName):
        knownLanguages = []
        for language in self.characters[characterName].languages:
            knownLanguages.append(language)
        return knownLanguages

    def setLanguages(self, characterName, language):
        self.characters[characterName].languages.append(language)

    def getOwner(self, characterName):
        return self.characters[characterName].owner

    def getActive(self, characterName):
        return self.characters[characterName].active

    def getName(self, characterName):
        return self.characters[characterName].name

    def getGold(self, characterName):
        return self.characters[characterName].gold

    def getHealth(self, characterName):
        return self.characters[characterName].health

    def getClass(self, characterName):
        return self.characters[characterName].characterClass


class Character:
    def __init__(self, name, owner, active):
        self.name = name
        self.owner = owner
        self.active = active
        self.stats = Stats()
        self.maxHealth = 10
        self.currentHealth = 10
        self.characterClass = characterClass("barbarian")
        self.level = 1
        self.race = "Not Set"
        self.gold = 0
        self.description = "Not Set"
        self.alignment = "Not Set"
        self.languages = []


class Stats:
    def __init__(self, stre=10, dex=10, con=10, inte=10, wis=10, cha=10):
        self.strength = stre
        self.dexterity = dex
        self.constitution = con
        self.intelligence = inte
        self.wisdom = wis
        self.charisma = cha

# TODO need to get all class / class info from website
class characterClass:
    classes = ("barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin",
               "ranger", "rogue", "sorcerer", "warlock", "wizard")

    def __init__(self, className):
        if className not in self.classes:
            raise ValueError("%s is not a valid class." % className)
        self.characterClass = className

# TODO need to get all skills form website
#class Skills:

#class Items:

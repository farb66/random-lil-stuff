import random
import enum

class TYPES(enum.Enum):
    ROCK : int = 1
    POP : int = 2
    RAP : int = 3

class attack:
    name : str
    type_attack : TYPES
    dmg : float

class banda: 
    name : str
    hp : float
    type_band : TYPES
    attacks = []
    
    def __init__(self, name, type_band):
        self.hp = 100
        self.name = name
        self.type_band = type_band

    def addAttack(self, name, type_attack, dmg): self.attacks.append(attack(name, type_attack, dmg))
    def attack(self): return random.choice(self.attacks)

class bandas(enum.Enum):
    #POP
    THE_CURE : banda = banda("The Cure", TYPES.POP)
    FLEETWOOD_MAC : banda = banda("Fleetwood Mac", TYPES.POP)
    ABBA : banda = banda("ABBA", TYPES.POP)
    COLDPLAY : banda = banda("ColdPlay", TYPES.POP)
    TAYTAY : banda = banda("Taylor Swift", TYPES.POP)
    OLIVIA : banda = banda("Olivia Rodrigo", TYPES.POP)

    #ROCK
    
def fight(attack, banda):
    #pop beats rock, rock beats rap, rap beats pop
    if attack.type_attack == banda.type_band: n = random.randint(0, 20)
    elif (attack.type_attack == 2 and banda.type_band == 1 or 
            attack.type_attack == 1 and banda.type_band == 3 or 
            attack.type_attack == 3 and banda.type_band == 2): n = random.randint(50, 100)
    else:  n = random.randint(0, 50)

    return attack.dmg - (attack.dmg*(random.randint(1, n)/100 )if n > 0 else 0)


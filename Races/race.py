from enum import Enum

class Size(Enum):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Alignment(Enum):
    LG = "Lawful good"
    NG = "Neutral good"
    CG = "Chaotic good"
    LN = "Lawful neutral"
    N = "Neutral"
    CN = "Chaotic neutral"
    LE = "Lawful evil"
    NE = "Neutral evil"
    CE = "Chaotic evil"
    
class Ability(Enum):
    STRENGTH = 0
    DEXTERITY = 1
    CONSTITUTION = 2
    INTELLIGENCE = 3
    WISDOM = 4
    CHARISMA = 5

class Race:
    
    name = ""
    adjective = ""
    description = ""
    
    size = ""
    alignments = ""
    
    ablility_modifiers = []
    skill_proficiencies = []
    
    def __init__(self, name, adjective, description, size, alignments, ablility_modifiers, skill_proficiencies) -> None:
        self.name = name
        self.adjective = adjective
        self.description = description
        self.size = size
        self.alignments = alignments
        self.ablility_modifiers = ablility_modifiers
        self.skill_proficiencies = skill_proficiencies
        
    def __str__(self) -> str:
        alignments = []
        for i in range(len(self.alignments)):
            alignments.append(self.alignments[i].value)
        
        ability_modifiers = []
        for i in range(len(self.ablility_modifiers)):
            if(self.ablility_modifiers[i] == 0):
                continue
            
            ability_modifiers.append([list(Ability)[i].name.title(), self.ablility_modifiers[i]])
        
        return "{}:\n{}\nSize: {}\nPossible alignments: \n{}\nAbility score modifiers: \n{}".format(self.name, self.description, self.size.value, alignments, ability_modifiers)
    
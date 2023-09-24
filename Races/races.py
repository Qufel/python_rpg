from race import Race, Size, Alignment

#Example
EXAMP = Race(
    "Human",
    ["human", "man"],
    "In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons. Perhaps it is because of their shorter lives that they strive to achieve as much as they can in the years they are given. Or maybe they feel they have something to prove to the elder races, and that's why they build their mighty empires on the foundation of conquest and trade. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.",
    Size.MEDIUM,
    list(Alignment),
    [2, -1, 0, 1, 0, 1],
    []
)

WORLD_RACES = [
    
]

print(EXAMP)
class Item:

    id = ""
    name = ""
    type = ""
    description = ""
    weight = 0
    
    def __init__(self, id = -1, name = "", description = "", weight = 0):
        self.id = id
        self.name = name
        self.type = type(self).__name__.title()
        self.description = description
        self.weight = weight

    def __str__(self) -> str:
        return "<== {} ==>\n{}\nType: {}\nWeight: {} lb".format(self.name, self.description, self.type, self.weight)
    
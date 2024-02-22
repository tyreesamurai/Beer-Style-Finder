class Recipe:
    name = ""
    category = ""
    recipe_type = ""
    fermentables = []
    hops = []
    other_ingredients = []
    yeast = ""
    instructions = ""
    notes = ""

    def __init__(self):
        pass

    def __str__(self):
        return self.name

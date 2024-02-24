class Recipe:
    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def set_recipe_type(self, recipe_type):
        self.recipe_type = recipe_type

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def set_procedure(self, procedure):
        self.procedure = procedure

    def set_id(self, id):
        self.id = id

    def check(self):
        if (
            hasattr(self, "name")
            and hasattr(self, "category")
            and hasattr(self, "recipe_type")
            and hasattr(self, "ingredients")
            and hasattr(self, "procedure")
            and hasattr(self, "id")
        ):
            return True
        else:
            return False


class Ingredients:
    def __init__(self):
        pass

    def set_fermentables(self, fermentables):
        self.fermentables = fermentables

    def set_hops(self, hops):
        self.hops = hops

    def set_yeast(self, yeast):
        self.yeast = yeast

    def set_other(self, other):
        self.other = other

    def check(self):
        if (
            hasattr(self, "fermentables")
            and hasattr(self, "hops")
            and hasattr(self, "yeast")
        ):
            return True
        else:
            return False

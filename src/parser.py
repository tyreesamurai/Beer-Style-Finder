from classes import Recipe, Ingredients

file = open("txtfiles/beer-recipe.txt", "r")

quick_reset = open("temp.txt", "w")
quick_reset.write("")
quick_reset.close()


def read_text(file):
    temp_file = None

    for line in file:
        if line.startswith("-") and (line.endswith("-") or line.endswith("-\n")):
            if temp_file:
                parse(temp_file)
                temp_file = None
            else:
                temp_file = open("temp.txt", "w")
                # temp_file.write("Starting here\n")

        if temp_file:
            temp_file.write(line)


def parse(file):
    # file.write("Break here\n")
    recipe = Recipe()
    ingredients = Ingredients()

    id_test = file.readline().split(" ").pop(1)
    if id_test.isdigit():
        recipe.set_id(id_test)

    recipe.set_name(file.readline())

    category_line = file.readline().title()

    if category_line.startswith("Category "):
        recipe.set_category(category_line.replace("Category ", ""))

    recipe_type_line = file.readline().title()

    if recipe_type_line.startswith("Recipe Type "):
        recipe.set_recipe_type(recipe_type_line.replace("Recipe Type ", ""))

    file.close()


read_text(file)

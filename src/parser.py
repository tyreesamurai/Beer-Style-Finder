from classes import Recipe, Ingredients

file = open("txtfiles/beer-recipe.txt", "r")

quick_reset = open("temp.txt", "w")
quick_reset.write("")
quick_reset.close()

recipe = Recipe()
ingredients = Ingredients()


def read_text(file):
    temp_file = None

    for line in file:
        if line.startswith("-") and (line.endswith("-") or line.endswith("-\n")):
            if temp_file:
                read_file = temp_file
                parse(read_file)
                temp_file = None
            else:
                temp_file = open("temp.txt", "a")
                temp_file.write("Starting here\n")

        if temp_file:
            temp_file.write(line)


def parse(file):
    # file.write("Break here\n")

    recipe_list = []
    recipe = Recipe()
    ingredients = Ingredients()

    while file:
        line = file.readline()
        match switch(line):
            case "id":
                recipe.set_id(line.split(" ").pop(1))
                recipe.set_name(file.readline().replace("\n", ""))
            case "category":
                replaced_text = line.replace("Category ", "")
                recipe.set_category(replaced_text.replace("\n", ""))
            case "recipe_type":
                replaced_text = line.replace("Recipe Type ", "")
                recipe.set_recipe_type(replaced_text.replace("\n", ""))
            case "fermentables":
                fermentables = []
                loop_line = file.readline()
                while switch(loop_line) == "none":
                    fermentables.append(loop_line.replace("\n", ""))
                    loop_line = file.readline()
                ingredients.set_fermentables(fermentables)
                switch(loop_line)
            case "hops":
                hops = []
                loop_line = file.readline()
                while switch(loop_line) == "none":
                    hops.append(loop_line)
                    loop_line = file.readline()
                ingredients.set_hops(hops)
                switch(loop_line)
            case "yeast":
                replaced_text = line.replace("Yeast ", "")
                ingredients.set_yeast(replaced_text.replace("\n", ""))
            case "other":
                other = []
                loop_line = file.readline()
                while switch(loop_line) == "none":
                    other.append(loop_line.replace("\n", ""))
                    loop_line = file.readline()
                ingredients.set_other(other)
                switch(loop_line)
            case "procedure":
                procedure = []
                procedure.append(line.replace("Procedure ", ""))
                loop_line = file.readline()
                while switch(loop_line) == "none":
                    procedure.append(loop_line.replace("\n", ""))
                    loop_line = file.readline()
                recipe.set_procedure(procedure)
                switch(loop_line)
            case "done":
                recipe.set_ingredients(ingredients)
                if ingredients.check() and recipe.check():
                    recipe_list.append(recipe)
                    recipe = Recipe()
                    ingredients = Ingredients()
                else:
                    if not ingredients.check():
                        print("Incorrect Ingredients for Recipe " + recipe.id + "\n")
                        print(vars(ingredients))
                        print("\n")
                    elif not recipe.check():
                        print("Incorrect Recipe for Recipe " + recipe.id + "\n")
                        print(vars(recipe))
                        print("\n")
                    recipe = Recipe()
                    ingredients = Ingredients()
            case "none":
                pass
            case "break":
                break

    file.close()
    return recipe_list


def switch(line):
    if line == "-----" or line == "-----\n":
        return "done"
    elif line.startswith("-") and line.endswith("-\n"):
        if line.split(" ").pop(1).isdigit():
            return "id"
    elif line.startswith("Category"):
        return "category"
    elif line.startswith("Recipe Type"):
        return "recipe_type"
    elif line.startswith("Fermentables"):
        return "fermentables"
    elif line.startswith("Hops"):
        return "hops"
    elif line.startswith("Yeast"):
        return "yeast"
    elif line.startswith("Other"):
        return "other"
    elif line.startswith("Procedure"):
        return "procedure"
    elif line == "" or line == "\n":
        return "break"
    else:
        return "none"


parse(file)

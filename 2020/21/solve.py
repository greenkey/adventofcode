import sys


def solve(file_name: str):
    food = list()
    for line in open(file_name).readlines():
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.strip().strip(')').split(', ')
        food.append((ingredients, allergens))

    allergens_set = dict()
    for ingredients, allergens in food:
        for allergen in allergens:
            if allergen not in allergens_set:
                allergens_set[allergen] = set(ingredients)
            else:
                allergens_set[allergen] = allergens_set[allergen].intersection(ingredients)
    allergens_set = [item for item in allergens_set.items()]
    identified_ingredients = set()
    allergen_ingredient = dict()
    while allergens_set:
        allergen, ingredients = allergens_set.pop(0)
        if len(ingredients) == 1:
            identified_ingredients.update(ingredients)
            allergen_ingredient[allergen] = ingredients.pop()
        else:
            allergens_set.append((allergen, ingredients.difference(identified_ingredients)))

    ingredients_with_allergens = set(allergen_ingredient.values())
    ingredients_without_allergens = set(i for ingredients, _ in food for i in ingredients if i not in ingredients_with_allergens)

    print(sum([len(ingredients_without_allergens.intersection(ingredients)) for ingredients, _ in food]))

    print(','.join(allergen_ingredient[a] for a in sorted(allergen_ingredient.keys())))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")

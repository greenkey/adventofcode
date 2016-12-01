from random import shuffle


def getScoreUsing(properties,ingredients, maxCalories=None):
    score = 1
    calories = 0
    tot = sum(ingredients.values())
    for i in ingredients.keys():
        ingredients[i] = int(round(  ingredients[i] * 100.0 / tot  ))
    for p in properties.keys():
        if p != "calories":
            propScore = 0
            for i in ingredients.keys():
                propScore += ingredients[i] * properties[p][i]
            score *= max(0,propScore)
        else:
            for i in ingredients.keys():
                calories += ingredients[i] * properties[p][i]

    print("With {}: {} ({} calories)".format(ingredients,score,calories))
    if calories > (maxCalories or calories):
        return None
    else:
        return score


if __name__ == "__main__":
    properties = {"capacity":dict(), "durability":dict(), "flavor":dict(), "texture":dict(), "calories":dict()}
    ingredients = dict()
    with open("input", "r") as ingredient_list:
        for ingredient in ingredient_list:
            (name,props) = ingredient.strip().split(":")
            ingredients[name] = 100
            # capacity 2, durability 3, flavor -2, texture -1, calories 3
            (capacity, durability, flavor, texture, calories) = props.split(",")
            properties["capacity"][name] =    int( capacity.split(" ")[2]   )
            properties["durability"][name] =  int( durability.split(" ")[2] )
            properties["flavor"][name] =      int( flavor.split(" ")[2]     )
            properties["texture"][name] =     int( texture.split(" ")[2]    )
            properties["calories"][name] =    int( calories.split(" ")[2]   )

    ings = ingredients.keys()
    for i in range(1,len(ings)):
        score = 0
        q = 0
        while True:
            ingredients[ings[i]] = q
            newScore = getScoreUsing(properties,ingredients,521) or score
            if newScore > score:
                score = newScore
            elif newScore < score:
                break
            q += 1
    tot = sum(ingredients.values())
    for i in ingredients.keys():
        ingredients[i] = int(round(  ingredients[i] * 100.0 / tot  ))
    getScoreUsing(properties,ingredients)

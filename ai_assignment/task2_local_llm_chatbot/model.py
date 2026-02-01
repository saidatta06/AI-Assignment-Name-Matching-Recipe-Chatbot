import json

with open("recipes.json") as f:
    RECIPES = json.load(f)

def suggest_recipe(user_ingredients):
    user_set = set(i.strip().lower() for i in user_ingredients)

    best_match = None
    best_score = 0

    for item in RECIPES:
        recipe_set = set(item["ingredients"])
        score = len(user_set & recipe_set)

        if score > best_score:
            best_score = score
            best_match = item["recipe"]

    if best_match:
        return best_match
    return "No matching recipe found."

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [obj["name"] for obj in spicy_foods]
    return names


def get_spiciest_foods(spicy_foods):
    names = [obj for obj in spicy_foods if obj["heat_level"] > 5]
    return names


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(
                f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
            )


def get_average_heat_level(spicy_foods):
    avg_heat = sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
    return avg_heat


def create_spicy_food(spicy_foods, spicy_food):
    food_list = spicy_foods
    food_list.append(spicy_food)
    return food_list
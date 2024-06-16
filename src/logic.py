def calculate_protein_target(weight):
    return weight * 2

    """
    Calculate the daily protein target based on the user's weight.

    Parameters:
    weight (float): The user's weight in kilograms.

    Returns:
    float: The daily protein target in grams.
    """
        


food_database = {
    'chicken breast': 31,
    'chicken thigh': 25,
    'chicken drumstick': 23,
    'tuna': 28,
    'egg': 6,
    'almonds': 21,
    'walnuts': 15,
    'protein shake': 25,
    'rice': 2.5,
    'pasta': 5,

    # Add more foods here
}

def add_meal(meals, food, amount):
    """
    Add a meal to the meals list and calculate its protein content.

    Parameters:
    meals (list): The list of meals.
    food (str): The name of the food item.
    amount (float): The amount of food in grams.

    Returns:
    float: The protein content of the meal.
    """
    protein = food_database.get(food, 0) * (amount / 100)
    meals.append((food, protein))
    return protein

def total_protein(meals):
    return sum(protein for _, protein in meals)
def remaining_protein(target, current):
    return target - current


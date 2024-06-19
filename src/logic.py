import os
import json

# Get the current directory of the file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to food_database.json
food_database_path = os.path.join(current_dir, 'food_database.json')

with open(food_database_path, 'r') as f:
    food_database = json.load(f)

def calculate_protein_target(weight):
    if weight <= 0:
        raise ValueError("Weight must be a positive number")

    return weight * 2

    """
    Calculate the daily protein target based on the user's weight.

    Parameters:
    weight (float): The user's weight in kilograms.

    Returns:
    float: The daily protein target in grams.

    Error: Raise error is weight entered is under or equal to 0 grams
    """

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

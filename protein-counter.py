def calculate_protein_target(weight):
    return weight * 2

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
    protein = food_database.get(food, 0) * (amount / 100)
    meals.append((food, protein))
    return protein

def total_protein(meals):
    return sum(protein for _, protein in meals)
def remaining_protein(target, current):
    return target - current

def main():
    weight = float(input("Enter your weight in kg: "))
    daily_target = calculate_protein_target(weight)
    print(f"Your daily protein target is {daily_target} grams.")

    meals = []
    while True:
        food = input("Enter the food you ate (or 'exit' to finish): ").lower()
        if food == 'exit':
            break
        amount = float(input(f"Enter the amount of {food} in grams: "))
        protein = add_meal(meals, food, amount)
        print(f"Added {protein} grams of protein from {food}.")
        current_protein = total_protein(meals)
        print(f"Total protein so far: {current_protein} grams.")
        print(f"You need {remaining_protein(daily_target, current_protein)} more grams to reach your target.")

if __name__ == "__main__":
    main()
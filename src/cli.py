from logic import calculate_protein_target, add_meal, total_protein, remaining_protein


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
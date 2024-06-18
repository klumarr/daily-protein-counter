import tkinter as tk
from tkinter import messagebox
from logic import calculate_protein_target, add_meal, total_protein, remaining_protein

class ProteinCounterApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Daily Protein Counter")


        # Create and pack the label for entering weight
        self.weight_label = tk.Label(root, text="Enter your weight (kg):")
        self.weight_label.pack()

        # Create and pack the entry widget for weight input
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        # Create and pack the button to set the protein target
        self.target_button = tk.Button(root, text="Set Target", command=self.set_target)
        self.target_button.pack()

        # Create and pack the label for entering meal details
        self.meal_label = tk.Label(root, text="Enter food and amount (e.g., 'chicken breast, 100'):",)
        self.meal_label.pack()

        # Create and pack the entry widget for meal input
        self.meal_entry = tk.Entry(root)
        self.meal_entry.pack()

        # Create and pack the button to add a meal
        self.add_button = tk.Button(root, text="Add Meal", command=self.add_meal)
        self.add_button.pack()


        # Create and pack the label to display total protein so far
        self.total_label = tk.Label(root, text="Total protein so far: 0 grams")
        self.total_label.pack()

        # Create and pack the label to display remaining protein needed
        self.remaining_label = tk.Label(root, text="Remaining protein: 0 grams")
        self.remaining_label.pack()


        # Initialize the meals list and daily target
        self.meals = []
        self.daily_target = 0

    def set_target(self):
        # Set the daily protein target based on weight input
        try:
            weight = float(self.weight_entry.get())
            self.daily_target = calculate_protein_target(weight)
            self.update_labels()
        except (IndexError, ValueError):
            # Show error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter a valid weight.")

    def add_meal(self):
        # Add a meal and update the labels
        try:
            meal_info = self.meal_entry.get().split(',')
            food = meal_info[0].strip().lower()
            amount = float(meal_info[1].strip())
            protein = add_meal(self.meals, food, amount)
            self.update_labels()
        except (IndexError, ValueError):
            # Show error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter the food and amount correctly")

    def update_labels(self):
        # Update the labels to reflect the current total and remaining protein
            current_protein = total_protein(self.meals)
            self.total_label.config(text=f"Total protein so far: {int(current_protein)} grams")
            self.remaining_label.config(text=f"Remaining protein: {int(remaining_protein(self.daily_target, current_protein))} grams")

if __name__ == "__main__":
    # Initialize and run the GUI application
    root = tk.Tk()
    app = ProteinCounterApp(root)
    root.mainloop()

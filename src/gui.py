import tkinter as tk
from tkinter import messagebox
from logic import calculate_protein_target, add_meal, total_protein, remaining_protein

class ProteinCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Protein Counter")

        self.weight_label = tk.Label(root, text="Enter your weight (kg):")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.target_button = tk.Button(root, text="Set Target", command=self.set_target)
        self.target_button.pack()

        self.meal_label = tk.Label(root, text="Enter food and amount (e.g., 'chicken breast, 100'):",)
        self.meal_label.pack()

        self.meal_entry = tk.Entry(root)
        self.meal_entry.pack()

        self.add_button = tk.Button(root, text="Add Meal", command=self.add_meal)
        self.add_button.pack()

        self.total_label = tk.Label(root, text="Total protein so far: 0 grams")
        self.total_label.pack()

        self.remaining_label = tk.Label(root, text="Remaining protein: 0 grams")
        self.remaining_label.pack()

        self.meals = []
        self.daily_target = 0

    def set_target(self):
        try:
            weight = float(self.weight_entry.get())
            self.daily_target = calculate_protein_target(weight)
            self.update_labels()
        except (IndexError, ValueError):
            messagebox.showerror("Invalid Input", "Please enter the food and amount correctly.")
    
    def add_meal(self):
        try:
            meal_info = self.meal_entry.get().split(',')
            food = meal_info[0].strip().lower()
            amount = float(meal_info[1].strip())
            protein = add_meal(self.meals, food, amount)
            self.update_labels()
        except (IndexError, ValueError):
            messagebox.showerror("Invalid Input", "Please enter the food and amount correctly")

    def update_labels(self):
        current_protein = total_protein(self.meals)
        self.total_label.config(text=f"Total protein so far: {current_protein} grams")
        self.remaining_label.config(text=f"Remaining protein: {remaining_protein(self.daily_target, current_protein)} grams")



root = tk.Tk()

app = ProteinCounterApp(root)

root.mainloop()
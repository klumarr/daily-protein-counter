# tests/test_logic.py

import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from logic import calculate_protein_target, add_meal, total_protein, remaining_protein

class TestLogicFunctions(unittest.TestCase):
    # Test the function that calculates daily protein target
    def test_calculate_protein_target(self):
        # Check standard cases
        self.assertEqual(calculate_protein_target(70), 140)  # 2 * 70 should be 140
        self.assertEqual(calculate_protein_target(50), 100)  # 2 * 50 should be 100
        # Check a negative case
        self.assertNotEqual(calculate_protein_target(70), 150)  # 2 * 70 should not be 150

    # Test the function that adds a meal and calculates protein
    def test_add_meal(self):
        meals = []
        protein = add_meal(meals, 'chicken breast', 100)
        self.assertEqual(protein, 31)  # 100g of chicken breast should be 31g of protein
        self.assertEqual(len(meals), 1)  # There should be 1 meal in the list
        self.assertEqual(meals[0][0], 'chicken breast')  # The meal should be 'chicken breast'
        self.assertEqual(meals[0][1], 31)  # The protein amount should be 31

        # Test with unknown food
        protein = add_meal(meals, 'unknown food', 100)
        self.assertEqual(protein, 0)  # Unknown food should have 0 protein
        self.assertEqual(len(meals), 2)  # There should be 2 meals in the list
        self.assertEqual(meals[1][0], 'unknown food')  # The second meal should be 'unknown food'
        self.assertEqual(meals[1][1], 0)  # The protein amount should be 0

    # Test the function that calculates total protein
    def test_total_protein(self):
        meals = [('chicken breast', 31), ('egg', 6)]
        self.assertEqual(total_protein(meals), 37)  # Total protein should be 31 + 6 = 37

        # Test with no meals
        meals = []
        self.assertEqual(total_protein(meals), 0)  # Total protein should be 0 with no meals

    # Test the function that calculates remaining protein needed
    def test_remaining_protein(self):
        self.assertEqual(remaining_protein(150, 50), 100)  # Remaining protein should be 100 (150 - 50)
        self.assertEqual(remaining_protein(100, 100), 0)  # Remaining protein should be 0 (100 - 100)
        self.assertEqual(remaining_protein(100, 150), -50)  # Remaining protein can be negative (-50)

    # Test invalid input for protein target calculation
    def test_invalid_weight_input(self):
        with self.assertRaises(ValueError):  # Check if ValueError is raised
            calculate_protein_target(-70)  # Negative weight should raise an error

if __name__ == '__main__':
    unittest.main()

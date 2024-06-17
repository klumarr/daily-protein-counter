# tests/test_logic.py

import unittest
import sys
import os

# Add the src directory to the sys.path or logic module cannot be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import functions from logic.py for testing
from logic import calculate_protein_target, add_meal, total_protein, remaining_protein

class TestLogicFunctions(unittest.TestCase):
    """
    TestLogicFunctions contains unit tests for functions defined in logic.py.
    Inherits from unittest.TestCase, which provides methods for assertions and test discovery.
    """

    def test_calculate_protein_target(self):
        """
        Tests the calculate_protein_target function to ensure it returns the correct protein target.
        """
        # Assert that the proteni targeet is correctly calculated
        self.assertEqual(calculate_protein_target(70), 140)
        self.assertEqual(calculate_protein_target(50), 100)
        # Assert that an incorrect value is not returned
        self.assertNotEqual(calculate_protein_target(70), 150)
    
    def test_add_meal(self):
        """
        Tests the add_meal function to ensure it correctly adds a meal and calculates its protein content.
        """
        meals = [] # Initialise an empty list for meals
        protein = add_meal(meals, 'chicken breast', 100) # Add 'chicken breast' with 100 grams
        # Assert that the protein content is correctly calculated
        self.assertEqual(protein, 31)
        # Assert that the meal has been added to the meals list
        self.assertEqual(len(meals), 1)
        # Assert that the first meal's name is 'chicken breast'
        self.assertEqual(meals[0][0], 'chicken breast')
        # Assert that the first meal's protein content is 31 grams
        self.assertEqual(meals[0][1], 31)
    
    def test_total_protein(self):
        """
        Tests the total_protein function to ensure it correctly sums up the protein from a list of meals.
        """
        meals = [('chicken breast', 31), ('egg', 6)] # List of meals with their protein content
        # Assert that the total protein content is correctly summed up
        self.assertEqual(total_protein(meals), 37)
    
    def test_remaining_protein(self):
        """
        Tests the remaining_protein function to ensure it correctly calculates the remaining protein needed.
        """
        # Asserts that the remaining protein content is correctly calculated
        self.assertEqual(remaining_protein(150, 50), 100)
        self.assertEqual(remaining_protein(100, 100), 0)

if __name__ == '__main__':
    # If this script is run directly, run the tests
    unittest.main()


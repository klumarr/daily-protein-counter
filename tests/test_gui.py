# Import necessary modules
import sys
import os
# Insert the src directory into the system path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch  # Import patch for mocking dependencies
from tkinter import Tk
from gui import ProteinCounterApp  # Import the GUI application to be tested

class TestGUI(unittest.TestCase):
    # Setup method to initialize the GUI application before each test
    def setUp(self):
        self.root = Tk()  # Create the root window for the Tkinter application
        self.app = ProteinCounterApp(self.root)  # Create an instance of the GUI application

    # Teardown method to destroy the GUI application after each test
    def tearDown(self):
        self.root.destroy()  # Destroy the root window to clean up after each test

    # Test the set_target method in the GUI
    @patch('logic.calculate_protein_target')  # Mock the calculate_protein_target function
    def test_set_target(self, mock_calculate_protein_target):
        mock_calculate_protein_target.return_value = 140  # Mock the return value to be 140 grams
        self.app.weight_entry.insert(0, '70')  # Simulate user input of '70' kg in the weight entry field
        self.app.set_target()  # Call the set_target method to set the daily protein target
        self.assertEqual(self.app.daily_target, 140)  # Assert that the daily target is set to 140 grams
        self.assertEqual(self.app.total_label['text'], 'Total protein so far: 0 grams')  # Check if total label is correct
        self.assertEqual(self.app.remaining_label['text'], 'Remaining protein: 140 grams')  # Check if remaining label is correct

    # Test the add_meal method in the GUI
    @patch('logic.add_meal')  # Mock the add_meal function
    @patch('logic.calculate_protein_target')  # Mock the calculate_protein_target function
    def test_add_meal(self, mock_calculate_protein_target, mock_add_meal):
        mock_calculate_protein_target.return_value = 140  # Mock the return value for calculate_protein_target
        self.app.weight_entry.insert(0, '70')  # Simulate user input of '70' kg in the weight entry field
        self.app.set_target()  # Call the set_target method to set the daily protein target

        mock_add_meal.return_value = 31  # Mock the return value for add_meal to be 31 grams of protein
        self.app.meal_entry.insert(0, 'chicken breast, 100')  # Simulate user input of 'chicken breast, 100' grams in the meal entry field
        self.app.add_meal()  # Call the add_meal method to add the meal
        self.assertEqual(self.app.meals[0], ('chicken breast', 31))  # Assert that the meal is added correctly
        self.assertEqual(self.app.total_label['text'], 'Total protein so far: 31 grams')  # Check if total label is updated correctly
        self.assertEqual(self.app.remaining_label['text'], 'Remaining protein: 109 grams')  # Check if remaining label is updated correctly

# Entry point to run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()  # Run all the test methods in this class

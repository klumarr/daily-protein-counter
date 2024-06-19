from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Get the absolute path to the directory where app.py is located
base_dir = os.path.abspath(os.path.dirname(__file__))

# Load food database from JSON file
food_database_path = os.path.join(base_dir, 'food_database.json')
with open(food_database_path, 'r') as f:
    food_database = json.load(f)

meals = []

# Your Edamam API credentials
EDAMAM_APP_ID = 'e43d46c1'
EDAMAM_APP_KEY = 'e43d46c1'

def get_protein_content(food_name):
    url = f"https://api.edamam.com/api/food-database/v2/parser"
    params = {
        'app_id': EDAMAM_APP_ID,
        'app_key': EDAMAM_APP_KEY,
        'ingr': food_name
    }
    response = requests.get(url, params=params)
    data = response.json()

    if 'parsed' in data and data['parsed']:
        food = data['parsed'][0]['food']
        nutrients = food['nutrients']
        protein_per_100g = nutrients.get('PROCNT', 0)  # Get protein content per 100g
        return protein_per_100g
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html', food_database=food_database, meals=meals)

@app.route('/add_meal', methods=['POST'])
def add_meal():
    food = request.form['food'].lower()
    amount = float(request.form['amount'])
    protein = food_database.get(food, 0) * (amount / 100)

    meals.append({'food': food, 'amount': amount, 'protein': protein})
    return redirect(url_for('index'))

@app.route('/new_food')
def new_food():
    return render_template('add_food.html')

@app.route('/add_food', methods=['POST'])
def add_food():
    food = request.form['food'].lower()
    protein = request.form['protein']

    # Check if protein was provided, if not fetch from API
    if not protein:
        protein = get_protein_content(food)
        if protein is None:
            flash('Could not find protein content for the entered food.')
            return redirect(url_for('new_food'))

    # Add the new food to the food database
    food_database[food] = float(protein)

    # Save the updated food database to the JSON file
    with open('food_database.json', 'w') as f:
        json.dump(food_database, f)

    flash('New food added successfully!')
    return redirect(url_for('index'))

@app.route('/delete_meal/<int:index>', methods=['POST'])
def delete_meal(index):
    if 0 <= index < len(meals):
        meals.pop(index)
    return redirect(url_for('index'))

@app.route('/edit_meal/<int:index>', methods=['GET', 'POST'])
def edit_meal(index):
    if request.method == 'POST':
        food = request.form['food'].lower()
        amount = float(request.form['amount'])
        protein = food_database.get(food, 0) * (amount / 100)

        meals[index] = {'food': food, 'amount': amount, 'protein': protein}
        return redirect(url_for('index'))

    meal = meals[index]
    return render_template('edit_meal.html', index=index, meal=meal, food_database=food_database)

if __name__ == "__main__":
    app.run(debug=True)

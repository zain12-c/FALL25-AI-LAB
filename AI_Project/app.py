from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


model = joblib.load("model.joblib")  

def categorize_food(desc):
    desc = desc.lower()
    if any(x in desc for x in ['chicken','beef','meat']):
        return 'Meat'
    elif any(x in desc for x in ['rice','bread','pasta']):
        return 'Carbs'
    elif any(x in desc for x in ['salad','vegetable','fruit']):
        return 'Veg'
    else:
        return 'Other'

@app.route("/", methods=["GET", "POST"])
def home():
    calories = None
    error_msg = None
    if request.method == "POST":
        meal_description = request.form.get("meal_description")
        cooking_method = request.form.get("cooking_method")

        food_category = categorize_food(meal_description)

        if food_category == "Other":
            error_msg = "⚠️ This does not seem like a valid food item. Please enter a proper meal."
        else:
            
            input_df = pd.DataFrame([{
                "meal_description": meal_description,
                "cooking_method": cooking_method,
                "food_category": food_category
            }])

           
            calories = model.predict(input_df)[0]
            calories = round(calories, 2)

    return render_template("index.html", calories=calories, error_msg=error_msg)


if __name__ == "__main__":
    app.run(debug=True)

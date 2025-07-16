import joblib
import os

# Safe loading with try-except
model_path = os.path.join("models", "nutrition_model.pkl")
try:
    model = joblib.load(model_path)
except Exception as e:
    model = None
    print("Model not loaded:", e)

def generate_meal_plan(user_input):
    if model:
        # Dummy input vector
        features = [len(user_input)]
        pred = model.predict([features])
        if pred[0] == 1:
            return [{"meal": "Lunch", "description": "Grilled chicken salad with avocado"}]
        else:
            return [{"meal": "Lunch", "description": "Lentil soup with quinoa"}]
    else:
        return [
            {"meal": "Breakfast", "description": "Oats with almonds and banana"},
            {"meal": "Lunch", "description": "Paneer wrap with spinach"},
            {"meal": "Dinner", "description": "Stir-fried tofu with rice"}
        ]

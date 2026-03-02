# promt.py

# Function to handle user queries about meal plans
def get_meal_plan(meal_type):
    meal_plans = {
        "breakfast": "For breakfast, I recommend oatmeal with fruits, a smoothie, or scrambled eggs with toast.",
        "lunch": "For lunch, how about a grilled chicken salad, a veggie wrap, or quinoa with roasted vegetables?",
        "dinner": "For dinner, you could have baked salmon with asparagus, a turkey burger, or a hearty vegetable soup.",
        "snack": "For a snack, enjoy a handful of almonds, a yogurt cup, or some carrot sticks with hummus."
    }

    # Fetch the meal plan based on the user's query
    return meal_plans.get(meal_type.lower(), "I'm sorry, I can only help with meal plans for breakfast, lunch, dinner, or snacks.")

# Example usage
if __name__ == "__main__":
    user_query = input("What meal would you like to plan? (e.g., breakfast, lunch, dinner, snack): ")
    print(get_meal_plan(user_query))
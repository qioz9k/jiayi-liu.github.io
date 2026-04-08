class food_item:
   
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat



def calculate_total_nutrition(food_list):
    total_cal = 0
    total_prot = 0
    total_carb = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_prot += food.protein
        total_carb += food.carbs
        total_fat += food.fat

    print("Total calories:", total_cal)
    print("Total protein (g):", total_prot)
    print("Total carbohydrates (g):", total_carb)
    print("Total fat (g):", total_fat)

    if total_cal > 2500:
        print("Warning: calories exceed 2500!")
    if total_fat > 90:
        print("Warning: fat exceeds 90g!")


if __name__ == "__main__":
  
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    banana = food_item("Banana", 90, 1.1, 23, 0.3)
    chicken = food_item("Chicken", 200, 30, 0, 8)

    meals = [apple, banana, chicken]

    calculate_total_nutrition(meals)
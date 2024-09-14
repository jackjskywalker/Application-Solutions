
class Recipe:
    def __init__(self, name, ingredients, cost_per_serving):
        self.name = name
        self.ingredients = ingredients
        self.cost_per_serving = cost_per_serving

class MealPrep:
    def __init__(self):
        self.recipes = {}
        self.meal_plan = {
            'Monday': {},
            'Tuesday': {},
            'Wednesday': {},
            'Thursday': {},
            'Friday': {},
            'Saturday': {},
            'Sunday': {}
        }

    def create_recipe(self):
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ").split(',')
        while True:
            try:
                cost_per_serving = float(input("Enter cost per serving: "))
                break
            except ValueError:
                print("Invalid input. Please enter a decimal number.")
        self.recipes[name] = Recipe(name, ingredients, cost_per_serving)
        print("Recipe created successfully!")

    def plan_meal(self):
        while True:
            recipe_name = input("Enter recipe name: ")
            if recipe_name in self.recipes:
                recipe = self.recipes[recipe_name]
                break
            else:
                print("Recipe not found. Please only enter existing recipe.")
        days = input("Enter days of the week (comma separated): ").split(',')
        for day in days:
            day = day.strip()
            while day not in self.meal_plan:
                print(f"Invalid day: {day}. Please try again.")
                day = input("Enter day of the week: ")
            while True:
                meal_type = input(f"Enter meal type (Breakfast, Lunch, Dinner) for {day}: ")
                meal_type = meal_type.capitalize()
                if meal_type in ['Breakfast', 'Lunch', 'Dinner']:
                    self.meal_plan[day][meal_type] = recipe
                    break
                else:
                    print("Invalid meal type. Please try again.")
        print("Meal planned successfully!")

    def display_recipes(self):
        print("\nAll Recipes:")
        for recipe in self.recipes.values():
            print(f"Name: {recipe.name}")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")
            print(f"Cost per serving: ${recipe.cost_per_serving:.2f}")
            print()

    def edit_recipe(self):
        recipe_name = input("Enter name of recipe to edit: ")
        if recipe_name in self.recipes:
            recipe = self.recipes[recipe_name]
            while True:
                print("\n1. Edit Name")
                print("2. Edit Ingredients")
                print("3. Edit Cost per Serving")
                print("4. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    recipe.name = input("Enter new name: ")
                    print("Name updated successfully!")
                elif choice == '2':
                    recipe.ingredients = input("Enter new ingredients (comma separated): ").split(',')
                    print("Ingredients updated successfully!")
                elif choice == '3':
                    while True:
                        try:
                            recipe.cost_per_serving = float(input("Enter new cost per serving: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a decimal number.")
                    print("Cost per serving updated successfully!")
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Recipe not found.")

    def delete_recipe(self):
        recipe_name = input("Enter name of recipe to delete: ")
        if recipe_name in self.recipes:
            del self.recipes[recipe_name]
            print("Recipe deleted successfully!")
        else:
            print("Recipe not found.")

    def display_meal_plan(self):
        total_cost = 0
        print("\nMeal Plan for the Week:")
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Meal Type', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
        for meal_type in ['Breakfast', 'Lunch', 'Dinner']:
            row = [meal_type]
            for day in self.meal_plan.keys():
                if meal_type in self.meal_plan[day]:
                    recipe = self.meal_plan[day][meal_type]
                    row.append(f"{recipe.name} (${recipe.cost_per_serving:.2f})")
                    total_cost += recipe.cost_per_serving
                else:
                    row.append('')
            print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
        print(f"Total cost for the week: ${total_cost:.2f}")

    def save(self):
        with open('recipes.txt', 'w') as f:
            for recipe in self.recipes.values():
                f.write(f"Recipe Name: {recipe.name}\n")
                f.write(f"Ingredients: {', '.join(recipe.ingredients)}\n")
                f.write(f"Cost: ${recipe.cost_per_serving:.2f}\n")
                f.write("-\n")
        with open('meal_plan.txt', 'w') as f:
            for day, meals in self.meal_plan.items():
                f.write(f"{day}\n")
                f.write("-\n")
                for meal_type, recipe in meals.items():
                    f.write(f"{meal_type}: {recipe.name}\n")
                f.write("\n")
        print("Recipes and meal plan saved successfully!")

    def load(self):
        try:
            with open('recipes.txt', 'r') as f:
                lines = f.readlines()
                for i in range(0, len(lines), 4):
                    name = lines[i].strip().split(': ')[1]
                    ingredients = lines[i+1].strip().split(': ')[1].split(', ')
                    cost_per_serving = float(lines[i+2].strip().split(': $')[1])
                    self.recipes[name] = Recipe(name, ingredients, cost_per_serving)
            with open('meal_plan.txt', 'r') as f:
                lines = f.readlines()
                day = None
                for line in lines:
                    line = line.strip()
                    if line in self.meal_plan:
                        day = line
                    elif line == '-':
                        continue
                    elif day:
                        meal_type, recipe_name = line.split(': ')
                        if recipe_name in self.recipes:
                            self.meal_plan[day][meal_type] = self.recipes[recipe_name]
            print("Recipes and meal plan loaded successfully!")
        except FileNotFoundError:
            print("No saved recipes or meal plan found.")

def main():
    meal_prep = MealPrep()
    while True:
        print("\n1. Create Recipe")
        print("2. Plan Meal")
        print("3. Display Recipes")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Display Meal Plan")
        print("7. Save")
        print("8. Load")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            meal_prep.create_recipe()
        elif choice == '2':
            meal_prep.plan_meal()
        elif choice == '3':
            meal_prep.display_recipes()
        elif choice == '4':
            meal_prep.edit_recipe()
        elif choice == '5':
            meal_prep.delete_recipe()
        elif choice == '6':
            meal_prep.display_meal_plan()
        elif choice == '7':
            meal_prep.save()
        elif choice == '8':
            meal_prep.load()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
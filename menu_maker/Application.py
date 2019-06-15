from flask import Flask, render_template, request
from .WeeklyMenu import WeeklyMenu 
from .Database import Database
import json

class AppData:
    def __init__(self):
        self.display_recipe_table = "none"
        self.menu = WeeklyMenu()

app = Flask(__name__)
app_data = AppData()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if request.form.get('generate_recipes') == "Generate recipes":
            app_data.menu.generateMeals()
        elif request.form.get('reroll.x'):
            day = request.form.get('day')
            meal = request.form.get('meal')
            app_data.menu.rerollMeal(day, meal)
        elif request.form.get('delete.x'):
            day = request.form.get('day')
            meal = request.form.get('meal')
            app_data.menu.deleteRecipe(day, meal)
            app_data.menu.rerollMeal(day, meal)


    return render_template('index.html', 
                            display_recipe_table=app_data.display_recipe_table,
                            menu_data=app_data.menu.menu,
                            menu_isset=app_data.menu.isset)



    

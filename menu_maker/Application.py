from flask import Flask, render_template, request
from .WeeklyMenu import WeeklyMenu 

class AppData:
    def __init__(self):
        self.display_recipe_table = "none"
        self.menu = WeeklyMenu()

app = Flask(__name__)
app_data = AppData()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        app_data.display_recipe_table = "none"
        pass
    elif request.method == 'POST':
        if request.form.get('generate_recipes') == "Generate recipes":
            app_data.menu.generateMeals()
            app_data.display_recipe_table = "contents"

    return render_template('index.html', 
                            display_recipe_table=app_data.display_recipe_table,
                            menu_data=app_data.menu.menu)



    

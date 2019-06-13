from flask import Flask, render_template, request
from .API import *

app = Flask(__name__)
display_recipe_table = "none"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        display_recipe_table = "none"
        pass
    elif request.method == 'POST':
        if request.form.get('generate_recipes') == "Generate recipes":
            getWeeklyMeals()
            display_recipe_table = "contents"

    return render_template('index.html', display_recipe_table=display_recipe_table)



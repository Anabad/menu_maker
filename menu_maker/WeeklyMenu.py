from .API import *

class WeeklyMenu:

    def __init__(self):
        
        self.menu = {
            "Monday":{
                "Lunch": None,
                "Dinner": None
            },
            "Tuesday":{
                "Lunch": None,
                "Dinner": None
            },
            "Wednesday":{
                "Lunch": None,
                "Dinner": None
            },
             "Thursday":{
                "Lunch": None,
                "Dinner": None
            },
             "Friday":{
                "Lunch": None,
                "Dinner": None
            },
             "Saturday":{
                "Lunch": None,
                "Dinner": None
            },
             "Sunday":{
                "Lunch": None,
                "Dinner": None
            },
        }
        
    def rerollMeal(self, day, meal):
        self.menu[day][meal] = getRandomRecipe()

    def generateMeals(self):
        self.menu = getWeeklyMeals()
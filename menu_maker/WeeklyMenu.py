from .API import API

class WeeklyMenu:

    def __init__(self):
        self.api = API()
        self.isset = False
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
        self.menu[day][meal] = self.api.getRandomRecipe()

    def generateMeals(self):
        self.menu = self.api.getWeeklyMeals()
        self.isset = True

    def deleteRecipe(self, day, meal):
        menuItem = self.menu[day][meal]
        self.api.delete(menuItem)
    
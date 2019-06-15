from .Database import Database
import random
class API:
    def __init__(self):
        self.database = Database()
        self.database.load("data/mydb.json")

    def getRandomRecipe(self):
        """ Return a random recipe from the database
        """
        recipe = random.choice(list(self.database.data.values()))

        return recipe

    def getWeeklyMeals(self):
        menu = {
                "Monday":{
                    "Lunch": None,
                    "Dinner": "Fish"
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
        for day in menu.values():
            day["Lunch"] = self.getRandomRecipe()
            day["Dinner"] = self.getRandomRecipe()
        return menu

    def delete(self, menuItem):
        self.database.data.pop(menuItem["id"])
        self.database.save(self.database.current_db_file)
        print(len(self.database.data))
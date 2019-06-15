import json
from progress.bar import Bar

class Database:

    def __init__(self):
        self.data = None
        self.current_db_file = None

    def load(self, dbfile):
        self.current_db_file = dbfile
        with open(dbfile) as db:    
            self.data = json.load(db)

    def save(self, dbfile, debug=False):
        with open(dbfile, "w") as db:
            if debug:
                indent = 4
            else:
                indent = None

            json.dump(self.data, db, indent=indent)

    def recompose(self):
        bar = Bar('Processing', max=len(self.data))
        for key, value in self.data.items():
            value["id"] = key
            value["url"] = f"http://www.bbc.co.uk/food/recipes/{'_'.join(key.split('_')[6:])}"
            if "t" in value.keys():
                value["title"] = value["t"]
                value.pop("t")
            if "p" in value.keys():
                value["preparationTime"] = value["p"]
                value.pop("p")
            if "c" in value.keys():
                value["cookingTime"] = value["c"]
                value.pop("c")
            if "l" in value.keys():
                value["numberOfIngredients"] = value["l"]
                value.pop("l")
            if "i" in value.keys() and value["i"]:
                value["image"] = f"//ichef.bbci.co.uk/food/ic/food_16x9_88/recipes/{'_'.join(key.split('_')[-2:])}_16x9.jpg"
                value.pop("i")
            if "v" in value.keys() and value["v"]:
                value["vegetarian"] = True
                value.pop("v")
            bar.next()
        bar.finish()
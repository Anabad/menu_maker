from menu_maker.Database import Database

db = Database()
db.load("data/titles.json")
db.recompose()
db.save("data/mydb.json")
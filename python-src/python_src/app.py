from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


my_recipe_ingredients = [
    {
        'id': 1,
        'name': 'Egg'
    },
    {
        'id': 2,
        'name': 'Bread'
    },
    {
        'id': 3,
        'name': 'Lettuce'
    },
    {
        'id': 4,
        'name': 'Cloves'
    },
    {
        'id': 5,
        'name': 'Tomato'
    },
    {
        'id': 6,
        'name': 'Spinach'
    },
    {
        'id': 7,
        'name': 'Carrot'
    },
]

@app.route("/recipes")
def recipes():
    recipes = {
        'egg_salad_sandwich': {
            'ingredient_ids': [
                1,2,3
            ]
        }
    }

    ingredient_ids = recipes['egg_salad_sandwich']['ingredient_ids']

    egg_salad_ingredients: list[str] = [item['name'] for item in my_recipe_ingredients if item['id'] in ingredient_ids]

    again_ingredients = []

    for item in my_recipe_ingredients:
        ingredient_name = item['name']
        ingredient_id = item['id']
        if ingredient_id in ingredient_ids:
            again_ingredients.append(ingredient_name)


    recipes['egg_salad_sandwich']['ingredients'] = again_ingredients

    return recipes
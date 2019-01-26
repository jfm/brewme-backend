import falcon
from brewme.api.recipes.operations import Recipes, RecipeByName
from falcon_prometheus import PrometheusMiddleware

def create():
    prometheus = PrometheusMiddleware()
    recipes = Recipes()
    recipe_by_name = RecipeByName()

    api = falcon.API(middleware=prometheus) 
    api.add_route('/metrics', prometheus)
    api.add_route('/recipes', recipes)
    api.add_route('/recipes/{name}', recipe_by_name)
    return api

api = application = create()

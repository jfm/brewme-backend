import falcon
from api.recipes.operations import Operations
from falcon_prometheus import PrometheusMiddleware

def create():
    prometheus = PrometheusMiddleware()
    recipes = Operations()
    api = falcon.API(middleware=prometheus) 
    api.add_route('/metrics', prometheus)
    api.add_route('/recipes', recipes)
    return api

api = application = create()

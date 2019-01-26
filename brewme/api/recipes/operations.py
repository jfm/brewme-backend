import falcon
import jsonpickle
from brewme.files.listing import Listing
from brewme.beerxml.parser import Parser

class Recipes(object):

    """Docstring for Operations. """

    def __init__(self):
        self.listing = Listing()
        self.parser = Parser()

    def on_get(self, request, response):
        recipes = []
        for recipe_file in self.listing.list_files_in_folder('/home/jfm/Repositories/brewme-backend/tests/recipes'):
            recipes_in_file = self.parser.parse_beerxml_file(recipe_file)
            recipes = recipes + recipes_in_file

        response.set_header('Access-Control-Allow-Origin', '*')
        response.body = jsonpickle.encode(recipes, unpicklable=False)
        response.status = falcon.HTTP_200

class RecipeByName(object):

    """Docstring for RecipeByName. """

    def __init__(self):
        """TODO: to be defined1. """
        self.listing = Listing()
        self.parser = Parser()

    def on_get(self, request, response, name):
        recipes = []
        result = None
        for recipe_file in self.listing.list_files_in_folder('/home/jfm/Repositories/brewme-backend/tests/recipes'):
            recipes_in_file = self.parser.parse_beerxml_file(recipe_file)
            recipes = recipes + recipes_in_file

        for recipe in recipes:
            if recipe.name == name:
                result = recipe

        response.set_header('Access-Control-Allow-Origin', '*')
        response.body = jsonpickle.encode(result, unpicklable=False)
        response.status = falcon.HTTP_200



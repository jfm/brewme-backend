import xmltodict
from brewme.beerxml.recipe import Recipe

class Parser(object):

    """Docstring for Parser. """

    def __init__(self):
        """TODO: to be defined1. """
        pass

    def parse_beerxml_file(self, path):
        with open(path) as file:
            beerxml_dict = xmltodict.parse(file.read())

        recipes = []
        #print(beerxml_dict['RECIPES'])
        for recipe_key, recipe_dict in beerxml_dict['RECIPES'].items():
            recipes.append(Recipe(recipe_dict))

        return recipes

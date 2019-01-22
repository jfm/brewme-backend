import pytest
from brewme.beerxml.parser import Parser

class TestParserClass:

    def test_parse_beerxml(self):
        parser = Parser()
        recipes = parser.parse_beerxml_file('tests/recipes/moerks-american-lager.xml')
        assert len(recipes) == 1
        assert len(recipes[0].hops) == 2
        assert len(recipes[0].fermentables) == 2
        assert len(recipes[0].yeasts) == 1
        assert len(recipes[0].mash.mash_steps) == 3
        assert recipes[0].name == 'Moerks American Lager'
        assert recipes[0].style.name == 'American Lager'
        assert recipes[0].equipment.name == 'Moerks Brewery'
        assert recipes[0].mash.name == 'Temperature Mash, 2 Step, Full Body'

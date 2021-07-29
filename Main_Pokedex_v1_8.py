from Collect_Pokedex_v1_8 import Collection
from Describe_Pokedex_v1_8 import Description
from Show_Pokedex_v1_8 import Presentation_Pokedex
from On_Pokedex_v1_8 import On_Pokedex
from Off_Pokedex_v1_8 import Off_Pokedex

class Pokedex:

    pokemons = dict()
    collected_pokemons = 0

    def __init__(self,name,height,type,behavior,pokemons = {},collected_pokemons = 1):
        self.name = name.title()
        self.height = height
        self.type = type.title()
        self.behavior = behavior.title() 
        self.pokemons = {}
        self.collected_pokemons = 1


On_Pokedex.on(Pokedex, Pokedex.collected_pokemons, Description.decribe,Collection.collect, Pokedex.pokemons, Presentation_Pokedex.show,Off_Pokedex.off)



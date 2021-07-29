class Collection:

    def collect(self,pokemons, collected_pokemons):
        pokemons.update({
        (collected_pokemons+1) : {
        'Name': self.name,
        'Height (cm)':int(self.height),
        'Type':self.type,
        'Behavior': self.behavior
        }
        })
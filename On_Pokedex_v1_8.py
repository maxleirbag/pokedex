class On_Pokedex:

    def on(self,collected_pokemons,describe,collect,pokemons,show,off):
        print("\n***POKEDEX***")
        while True:
            collected_pokemons += 1
            info_name = input("What's the pokemon's name? ")
            info_height = input("What's the pokemon's height (cm)? ")
            info_type = input("What's the pokemon's type? ")
            info_behavior = input("What's the pokemon's behavior like? ")
            new_pokemon = self(info_name,info_height,info_type,info_behavior)
            describe(new_pokemon, collected_pokemons)
            collect(new_pokemon,pokemons, collected_pokemons)
        
            creativity = int(input('Do you want do add a new pokemon to your Pokedex? (1: Yes / 2: No) \nPress the number:'))
            if (creativity != 1):
                break
        show(pokemons)
        off()
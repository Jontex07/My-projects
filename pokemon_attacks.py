from  pokemon_class import *
#low tier under 350
#mid tier between 351 t0 500
#high tier above 501
class Low_tier_attacks(Pokemon):
    pass



def main_pokemon_attack():
    low_tier = []
    mid_tier = []
    high_tier = []
    allpokemons = All_Pokemons("pokemon_list.csv")
    for pokemon in allpokemons.pokemon_list:
        if pokemon.Total <= 350:
            low_tier.append(pokemon)
        elif pokemon.Total > 350 and pokemon.Total <= 500:
            mid_tier.append(pokemon)
        elif pokemon.Total > 500:
            high_tier.append(pokemon)




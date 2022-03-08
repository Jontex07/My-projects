import csv
import random


class Pokemon:#a class that represent each pokemon
    def __init__(self, pokemon: list):
        self.num = self.__check_int(pokemon[0])
        self.Name = pokemon[1]
        self.Type_1 = self.check_type(pokemon[2])
        self.Type_2 = self.check_type(pokemon[3])
        self.Total = self.__check_int(pokemon[4])
        self.HP = self.__check_int(pokemon[5])
        self.Atk = self.__check_int(pokemon[6])
        self.Def = self.__check_int(pokemon[7])
        self.Sp_Atk = self.__check_int(pokemon[8])
        self.Sp_Def = self.__check_int(pokemon[9])
        self.Speed = self.__check_int(pokemon[10])
        self.attacks = self.attack_pool()
        self.Gen = self.__check_int(pokemon[11])
        self.Leg = pokemon[12]
    def check_type(self,type):#make sure that a pokemon has a type
        if type == None:
            return "no type"
        else:
            return type

    def __check_int(self, num):#converting the stats to int
        new_num = int(num)
        return new_num

    def attack_pool(self):#catgorais a pokemon and give attacks by tire
        if self.Total <= 350:
            pool_dict = {"Tackle (Normal)":40}
            if self.Type_1 == "Fire":
                pool_dict["Ember (Fire)"] = 40
                return pool_dict
            if self.Type_1 == "Water":
                pool_dict["Water gun (Water)"] = 40
                return pool_dict
            if self.Type_1 == "Bug":
                pool_dict["Fury Cutter (Bug)"] = 40
                return pool_dict
            if self.Type_1 == "Dragon":
                pool_dict["Dual Chop (Dragon)"] = 40
                return pool_dict
            if self.Type_1 == "Electric":
                pool_dict["Nuzzle (Electric)"] = 20
                return pool_dict
            if self.Type_1 == "Fighting":
                pool_dict["Mach Punch (Fighting)"] = 40
                return pool_dict
            if self.Type_1 == "Flying":
                pool_dict["Peck (Flying)"] = 35
                return pool_dict
            if self.Type_1 == "Ghost":
                pool_dict["Shadow Sneak (Ghost)"] = 40
                return pool_dict
            if self.Type_1 == "Grass":
                pool_dict["Mega Drain (Grass)"] = 40
                return pool_dict
            if self.Type_1 == "Ground":
                pool_dict["Sand Tomb (Ground)"] = 35
                return pool_dict
            if self.Type_1 == "Ice":
                pool_dict["Ice Ball (Ice)"] = 30
            if self.Type_1 == "Normal":
                pool_dict["Quick Attack (Normal)"] = 40
                return pool_dict
            if self.Type_1 == "Poison":
                pool_dict["Smog (Poison)"] = 30
                return pool_dict
            if self.Type_1 == "Psychic":
                pool_dict["Teleport (Psychic)"] = 0
                return pool_dict
            if self.Type_1 == "Rock":
                pool_dict["Rock Blast (Rock)"]= 35
                return pool_dict
        elif self.Total >500:
            pool_dict = {"Horn Attack (Normal)": 65}
            if self.Type_1 == "Fire":
                pool_dict["Rock Slide (Rock)"] = 75
                pool_dict["Flamethrower (Fire)"] = 90
                pool_dict["Blast Burn (Fire)"] = 150
                return pool_dict
            if self.Type_1 == "Water":
                pool_dict["Hydro Cannon (Water)"] = 150
                pool_dict["Ice Beam (Ice)"] = 90
                pool_dict["Surf (Water)"] = 90
                return pool_dict
            if self.Type_1 == "Bug":
                pool_dict["Fury Cutter (Bug)"] = 40
                pool_dict["Giga Drain (Grass)"] = 75
                pool_dict["Bug Buzz (Bug)"] = 90
                return pool_dict
            if self.Type_1 == "Dragon":
                pool_dict["Draco Meteor (Dragon)"] = 130
                pool_dict["Thunderbolt (Electric)"] = 90
                pool_dict["Dragon Claw (Dragon)"] = 80
                return pool_dict
            if self.Type_1 == "Electric":
                pool_dict["Thunderbolt (Electric)"] = 90
                pool_dict["Shadow Ball (Ghost)"] = 80
                pool_dict["Zap Cannon (Electric)"] = 120
                return pool_dict
            if self.Type_1 == "Fighting":
                pool_dict["Focus Punch (Fighting)"] = 150
                pool_dict["Rock Slide (Rock)"] = 75
                pool_dict["Revenge (Fighting)"] = 60
                return pool_dict
            if self.Type_1 == "Flying":
                pool_dict["Brave Bird (Flying)"] = 120
                pool_dict["Thunderbolt (Electric)"] = 90
                pool_dict["Fly (Flying)"] = 90
                return pool_dict
            if self.Type_1 == "Ghost":
                pool_dict["Shadow Ball (Ghost)"] = 80
                pool_dict["Moongeist Beam (Ghost)"] = 100
                pool_dict["Psybeam (Psychic)"] = 65
                return pool_dict
            if self.Type_1 == "Grass":
                pool_dict["Frenzy Plant (Grass)"] = 150
                pool_dict["Earthquake (Ground)"] = 100
                pool_dict["Solar Beam (grass)"] = 120
                return pool_dict
            if self.Type_1 == "Ground":
                pool_dict["Earthquake (Ground)"] = 100
                pool_dict["Stone Edge (Rock)"] = 90
                pool_dict["Mud Bomb"] = 65
                return pool_dict
            if self.Type_1 == "Ice":
                pool_dict["Blizzard (Ice)"] = 110
                pool_dict["Water Pulse (Water)"] = 60
                pool_dict["Ice Beam (Ice)"] = 90
                return pool_dict
            if self.Type_1 == "Normal":
                pool_dict["Quick Attack (Normal)"] = 40
                pool_dict["Dig (Ground)"] = 80
                pool_dict["Hyper Beam (Normal)"] = 150
                return pool_dict
            if self.Type_1 == "Poison":
                pool_dict["Gunk Shot (Poison)"] = 120
                pool_dict["Earthquake (Ground)"] = 100
                pool_dict["Cross Poison (poison)"] = 70
                return pool_dict
            if self.Type_1 == "Psychic":
                pool_dict["Ice Punch (Ice)"] = 75
                pool_dict["Future Sight (Psychic)"] = 120
                pool_dict["Fire Punch"] = 75
                return pool_dict
            if self.Type_1 == "Rock":
                pool_dict["Stone Edge (Rock)"] = 100
                pool_dict["Dig [Ground]"] = 80
                pool_dict["Rock Slide (Rock)"] = 75
                return pool_dict
        elif self.Total >350 and self.Total <=500:
             pool_dict = {"Horn Attack (Normal)": 65}
             if self.Type_1 == "Fire":
                 pool_dict["Snarl (Dark)"] = 55
                 pool_dict["Flame Charge (Fire)"] = 50
                 pool_dict["Flamethrower (Fire)"] = 90
                 return pool_dict
             if self.Type_1 == "Water":
                 pool_dict["Water gun (Water)"] = 40
                 pool_dict["Ice Shard (Ice)"] = 40
                 pool_dict["Surf (Water)"] = 90
                 return pool_dict
             if self.Type_1 == "Bug":
                 pool_dict["Fury Cutter (Bug)"] = 40
                 pool_dict["Absorb (Grass)"] = 20
                 pool_dict["Signal Beam (Bug)"] = 75
                 return pool_dict
             if self.Type_1 == "Dragon":
                 pool_dict["Dual Chop (Dragon)"] = 40
                 pool_dict["Spark (Electric)"] = 65
                 pool_dict["Dragon Claw (Dragon)"] = 80
                 return pool_dict
             if self.Type_1 == "Electric":
                 pool_dict["Nuzzle (Electric)"] = 20
                 pool_dict["Shadow Sneak (Ghost)"] = 40
                 pool_dict["Volt Switch (Electric)"] = 70
                 return pool_dict
             if self.Type_1 == "Fighting":
                 pool_dict["Mach Punch (Fighting)"] = 40
                 pool_dict["Rock Throw (Rock)"] = 50
                 pool_dict["Revenge (Fighting)"] = 60
                 return pool_dict
             if self.Type_1 == "Flying":
                 pool_dict["Peck (Flying)"] = 35
                 pool_dict["Ice Ball (Ice)"] = 30
                 pool_dict["Fly (Flying)"] = 90
                 return pool_dict
             if self.Type_1 == "Ghost":
                 pool_dict["Shadow Sneak (Ghost)"] = 40
                 pool_dict["Ominous Wind (Ghost)"] = 60
                 pool_dict["Psybeam (Psychic)"] = 65
                 return pool_dict
             if self.Type_1 == "Grass":
                 pool_dict["Mega Drain (Grass)"] = 40
                 pool_dict["Poison Fang (Poison)"] = 50
                 pool_dict["Razor Leaf (grass)"] = 55
                 return pool_dict
             if self.Type_1 == "Ground":
                 pool_dict["Sand Tomb (Ground)"] = 35
                 pool_dict["Rock Throw (Rock)"] = 50
                 pool_dict["Mud Bomb"] = 65
                 return pool_dict
             if self.Type_1 == "Ice":
                 pool_dict["Ice Ball (Ice)"] = 30
                 pool_dict["Water Pulse (Water)"] = 60
                 pool_dict["Ice Beam (Ice)"] = 90
                 return pool_dict
             if self.Type_1 == "Normal":
                 pool_dict["Quick Attack (Normal)"] = 40
                 pool_dict["Dig [Ground]"] = 80
                 pool_dict["Swift [Normal]"] = 60
                 return pool_dict
             if self.Type_1 == "Poison":
                 pool_dict["Smog (Poison)"] = 30
                 pool_dict["Mud Shot (Ground)"] = 55
                 pool_dict["Cross Poison (poison)"] = 70
                 return pool_dict
             if self.Type_1 == "Psychic":
                 pool_dict["Teleport (Psychic)"] = 0
                 pool_dict["Zen Headbutt (Psychic)"] = 80
                 pool_dict["Fire Punch"] = 75
                 return pool_dict
             if self.Type_1 == "Rock":
                 pool_dict["Rock Blast (Rock)"] = 35
                 pool_dict["Dig [Ground]"] = 80
                 pool_dict["Rock Slide (Rock)"] = 75
                 return pool_dict

    def print_attacks(self):
        back = ""
        key_list = list(self.attacks.keys())
        values_list = list(self.attacks.values())
        if len(key_list) == 2:
            back = "1."+key_list[0]+"   "+str(values_list[0])+"\n"+"2."+key_list[1]+"   "+str(values_list[1])
        elif len(key_list) == 4:
            back = "1."+key_list[0]+"   "+str(values_list[0])+"\n"+"2."+key_list[1]+"   "+str(values_list[1])\
                    +"\n3." + key_list[2] + "   " + str(values_list[2]) + "\n" + "4." + key_list[3] + "   " + str(
                        values_list[3])
        return back



    def __str__(self):
        back = "Name: " + self.Name + "\n Type: " + self.Type_1 + " " + self.Type_2
        return back

    def __repr__(self):
        return str(self)


class All_Pokemons():
    def __init__(self, name):
        self.pokemon_list = list()
        self.fire = list()

        with open(name) as csvfile:
            read = csv.reader(csvfile)
            next(read)
            for row in read:
                new_pokemon = Pokemon(row)
                self.pokemon_list.append(new_pokemon)

    def print_me(self):
        for row in self.pokemon_list:
            print(row)

    def check_name(self, name):
        new_name = str(name).title()
        for pokemon in self.pokemon_list:
            if pokemon.Name == new_name:
                return pokemon

    def pokemon_battle(self, pokemon1: Pokemon, pokemon2: Pokemon):
        if pokemon1.Total > pokemon2.Total:
            return print(self.print_pokmon(pokemon1) + "\nVS\n" + self.print_pokmon(
                pokemon2) + "\n and the winner is " + pokemon1.Name + "!!!!!")
        else:
            return print(self.print_pokmon(pokemon1) + "VS" + self.print_pokmon(
                pokemon2) + "\nand the winner is " + pokemon2.Name + "!!!!!")

    def print_pokmon(self,num):
        back = "no pokemons by this number"
        for pokemon in self.pokemon_list:
            if num == int(pokemon.num):
                back = pokemon.Name + "\n" + pokemon.Type_1 + " " + pokemon.Type_2 + "\n" + str(pokemon.Total)
        return print(back)

    def select_a_pokemon(self,num):
        for pokemon in self.pokemon_list:
            if num == pokemon.num:
                return pokemon


    def super_effective(self, p1:Pokemon, p2: Pokemon):
        if p1.Type_1 == "Fire" or p1.Type_2 == "Fire":
            if p2.Type_1 == "Water" or p2.Type_1 == "Ground" or p2.Type_1 == "Rock" or p2.Type_2 == "Water" or p2.Type_2 == "Ground" or p2.Type_2 == "Rock":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Grass" or "Ice" or "BUG" or p2.Type_2 == "Grass" or p2.Type_2 == "Ice" or p2.Type_2 == "BUG":
                for val in p1.attacks.values():
                    val *= 1.25
        else:
            pass

        if p1.Type_1 == "Water" or p1.Type_2 == "Water":
            if p2.Type_1 == "Grass" or p2.Type_1 == "Electric" or p2.Type_2 == "Grass" or p2.Type_2 == "Electric":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Fire" or p2.Type_1 == "Ground" or p2.Type_2 == "Fire" or p2.Type_2 == "Ground":
                for val in p1.attacks.values():
                    val *= 1.25

            else:
                pass

        if p1.Type_1 == "Grass" or p1.Type_2 == "Grass":
            if p2.Type_1 == "Fire" or p2.Type_2 == "Ice" or p2.Type_1 == "Poison" or p2.Type_1 == "Flying" or p2.Type_1 == "Bug" \
                    or p2.Type_2 == "Fire" or p2.Type_2 == "Ice" or p2.Type_2 == "Poison" or p2.Type_2 == "Bug":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Water" or p2.Type_1 == "Ground" or p2.Type_1 == "Rock" or p2.Type_2 == "Water" or \
                    p2.Type_2 == "Ground" or p2.Type_2 == "Rock":
                for val in p1.attacks.values():
                    val *= 1.25
        else:
            pass

        if p1.Type_1 == "Normal" or p1.Type_2 == "Normal":
            if p2.Type_1 == "Fighting" or p2.Type_2 == "Fighting":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Fire" or p2.Type_1 == "Ground" or p2.Type_2 == "Fire" or p2.Type_2 == "Ground":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Ice" or p1.Type_2 == "Ice":
            if p2.Type_1 == "Fighting" or p2.Type_1 == "Fire" or p2.Type_1 == "Rock" or p2.Type_2 == "Fighting" \
                    or p2.Type_2 == "Fire" or p2.Type_2 == "Rock":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Grass" or p2.Type_1 == "Ground" or p2.Type_2 == "Flying" or p2.Type_1 == "Dragon" or \
                    p2.Type_2 == "Grass" or p2.Type_2 == "Ground" or p2.Type_2 == "Flying" or p2.Type_2 == "Dragon":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass
        if p1.Type_1 == "Electric" or p1.Type_2 == "Electric":
            if p2.Type_1 == "Ground" or p2.Type_2 == "Ground":
                for val in p2.attacks.values():
                    val*= 1.25

            elif p2.Type_1 == "Water" or p2.Type_1 == "Flying" or p2.Type_2 == "Water" or p2.Type_2 == "Flying":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Poison" or p1.Type_2 == "Poison":
            if p2.Type_1 == "Ground" or p2.Type_1 == "Psychic" or p2.Type_2 == "Ground" or p2.Type_2 == "Psychic":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Grass" or p2.Type_2 == "Grass":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Ground" or p1.Type_2 == "Ground":
            if p2.Type_1 == "Water" or p2.Type_1 == "Grass" or p2.Type_1 == "Ice" or p2.Type_2 == "Water" or p2.Type_2 == "Grass" \
                    or p2.Type_2 == "Ice":
                for val in p2.attacks.values():
                    val *= 1.25
            elif p2.Type_1 == "Fire" or p2.Type_1 == "Electric" or p2.Type_1 == "Poison" or p2.Type_2 == "Rock" or \
                    p2.Type_2 == "Fire" or p2.Type_2 == "Electric" or p2.Type_2 == "Poison" or p2.Type_2 == "Rock":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Flying" or p1.Type_2 == "Flying":
            if p2.Type_1 == "Electric" or p2.Type_1 == "Ice" or p2.Type_1 == "Rock" or \
                    p2.Type_2 == "Electric" or p2.Type_2 == "Ice" or p2.Type_2 == "Rock":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Grass" or p2.Type_1 == "Fighting" or p2.Type_1 == "Bug" or p2.Type_2 == "Grass" or \
                    p2.Type_2 == "Fighting" or p2.Type_2 == "Bug":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Psychic" or p1.Type_2 == "Psychic":
            if p2.Type_1 == "Bug" or p2.Type_1 == "Ghost" or p2.Type_2 == "Bug" or p2.Type_2 == "Ghost":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Fighting" or p2.Type_1 == "Poison" or p2.Type_2 == "Fighting" or p2.Type_2 == "Poison":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Bug" or p1.Type_2 == "Bug":
            if p2.Type_1 == "Fire" or p2.Type_1 == "Flying" or p2.Type_1 == "Rock" or p2.Type_2 \
                    == "Fire" or p2.Type_2 == "Flying" or p2.Type_2 == "Rock":
                for val in p2.attacks.values():
                    val *= 1.25
            elif p2.Type_1 == "Grass" or p2.Type_1 == "Psychic" or p2.Type_2 == "Grass" or p2.Type_2 == "`Psychic":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Rock" or p1.Type_2 == "Rock":
            if p2.Type_1 == "Water" or p2.Type_1 == "Grass" or p2.Type_1 == "Fighting" or p2.Type_1 \
                    == "Ground" or p2.Type_2 == "Water" or p2.Type_2 == "Grass" or p2.Type_2 == "Fighting`" or p2.Type_2 \
                    == "Ground":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Fire" or p2.Type_1 == "Ice" or p2.Type_1 == "Flying" \
                    or p2.Type_1 == " Bug" or p2.Type_2 == "Fire" or p2.Type_2 == "Ice" or p2.Type_2 == "`Flying" \
                    or p2.Type_2 == "Bug":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Ghost" or p1.Type_2 == "Ghost":
            if p2.Type_1 == "Ghost" or p2.Type_2 == "Ghost":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Ghost" or p2.Type_1 == "Psychic" or p2.Type_2 == "Ghost" or p2.Type_2 == "`Psychic":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        if p1.Type_1 == "Dragon" or p1.Type_2 == "Dragon":
            if p2.Type_1 == "Dragon" or p2.Type_1 == "Ice" or p2.Type_2 \
                    == "Dragon" or p2.Type_2 == "Ice":
                for val in p2.attacks.values():
                    val *= 1.25

            elif p2.Type_1 == "Dragon" or p2.Type_2 == "Dragon":
                for val in p1.attacks.values():
                    val *= 1.25
            else:
                pass

        return p1, p2







# if __name__ == '__main__':
#     pokemon_list1 = All_Pokemons("pokemon_list.csv")
#     pokemon_list1.print_me()
#     player_1 = random.choice(pokemon_list1.pokemon_list)
#     step_1 = pokemon_list1.check_name(player_1)
#     pokemon_list1.print_me()
#     player_2 = input("Ok now it's your turn to choose a pokemon :")
#     step_2 = pokemon_list1.check_name(player_2)
#     battle = pokemon_list1.super_effective(step_1, step_2)
#     print(pokemon_list1.pokemon_battle(battle[0], battle[1]))


# all_pokemons = All_Pokemons("pokemon_list.csv")
# pokemon1 = all_pokemons.select_a_pokemon(6)
# x = pokemon1.print_attacks()
# # print(pokemon1.attacks.values())


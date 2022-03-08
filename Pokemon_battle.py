from pokemon_class import *
import random
# def Pokemon_battle(p1,p2):
#     if p1.Speed > p2.Speed:
#         print(p1.Name+" Attacks!")
#         p2.Total = p2.Total - p1.Atk
#         if p2.Total > 0:
#             print(p2.Name + " Attacks!")
#             p1.Total = p1.Total - p2.Atk
#             if p1.Total <= 0:
#               p1.Total = 0
#               print(p1.Name + " Fainted!! " + p2.Name + " is the winner!")
#         elif  p2.Total <= 0:
#             p2.Total = 0
#             print(p2.Name + " Fainted!! " + p1.Name + " is the winner!")
#         print(p1.Name+" HP:"+str(p1.Total)+"\n"+p2.Name+" HP: "+str(p2.Total))
#     elif p2.Speed > p1.Speed:
#         print(p2.Name + " Attacks!")
#         p1.Total = p1.Total - p2.Atk
#         if p1.Total > 0:
#             print(p1.Name + " Attacks!")
#             p2.Total = p2.Total - p1.Atk
#             if p2.Total <= 0:
#               p2.Total = 0
#               print(p2.Name + " Fainted!! " + p1.Name + " is the winner!")
#         elif p1.Total <= 0:
#             p1.Total = 0
#             print(p1.Name + " Fainted!! " + p2.Name + " is the winner!")
#         print(p1.Name+" HP:"+str(p1.Total)+"\n"+str(p2.Name)+" HP: "+str(p2.Total))
#     return p1,p2
def Pokemon_battle(p1:Pokemon,p2:Pokemon):
    p1_attack_pool = []
    p2_attack_pool = []
    for a in p1.attacks.keys():
        p1_attack_pool.append(a)
    for b in p2.attacks.keys():
        p2_attack_pool.append(b)



    while p1.Total >0 and p2.Total > 0:
        if p1.Speed > p2.Speed:
            print(p1.Name+" HP:"+str(p1.Total))
            print(p2.Name+" HP:"+str(p2.Total))
            print("Your Turn to Attack! ")
            atc1 = input(p1.print_attacks()+"\n select your move:")
            print(p1.Name+" used "+p1_attack_pool[int(atc1)-1])
            p2.Total -= p1.attacks[p1_attack_pool[int(atc1)-1]]
            if p2.Total <=0:
                break
            print("now player2 will attack")
            p1.Total-=p2.Atk
            if p1.Total<=0:
                break
            return Pokemon_battle(p1,p2)
        if p2.Speed > p1.Speed:
            print(p1.Name + " HP:" + str(p1.Total))
            print(p2.Name + " HP:" + str(p2.Total))
            print(p2.Name+" used "+p2_attack_pool[random.randint(0,4)-1])
            p1.Total-=p2.Atk
            if p1.Total<=0:
                break
            print("now its your turn' select your move")
            input(p1.print_attacks()+"\nselect:")
            p2.Total-=p1.Atk
            if p2.Total <=0:
                break
            return Pokemon_battle(p1,p2)

    if p1.Total <=0:
        print(p1.Name+" fainted!")
        print("And the winner is player2 and "+p2.Name)
    elif p2.Total <=0:
        print(p2.Name + " fainted!")
        print("And the winner is player1 and "+p1.Name)














if __name__ == '__main__':
    pokemon_list1 = All_Pokemons("pokemon_list.csv")
    #the computer selects his pokemon
    player_1 = random.choice(pokemon_list1.pokemon_list)
    player_1_scery = print("you have no chance aginst my "+player_1.Name)
    player_2 = input("Ok now it's your turn please choose a pokemon: ")
    step_2 = pokemon_list1.check_name(player_2)
    battle = pokemon_list1.super_effective(player_1, step_2)
    pokemon_1 = battle[0]
    pokemon_2 = battle[1]
    x = Pokemon_battle(pokemon_1,pokemon_2)
    # while x[0].Total > 0 and x[1].Total > 0:
    #     y = Pokemon_battle(x[0],x[1])













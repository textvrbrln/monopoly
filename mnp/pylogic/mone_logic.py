#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import dice
import streets
import player

'''Start event loop'''

def get_player_ready():    
        playerlist_length = len(player.playerlist)
        element = 0
        #for elements in list(range(1,playerlist_length)):
        while element <= playerlist_length:
            playername = player.playerlist[element]
            play(playername)
            decision = input("Nächster Spieler?[Y/N]")
            if decision == "Y":
                element += 1
                print(element)
                print(playerlist_length)
                if element >= playerlist_length:
                    get_player_ready()
            elif decision == "N":
                exit

def play(playername):
    # 
    print("Dice")
    print(playername)

    # throw_dice and move to field number X
    go_to_field = dice.move_forward()
    
    # check for double
    doublecheck = dice.double[0]
    if doublecheck == 1:
        print("Pasch!")
        # a) User plays again
        # b) User goes to Jail
    else:
        pass
    
    # go_to_field = 0
    #print("Feld", go_to_field)
    
    # If move-to-field is a street...
    if dice.get_field_type(go_to_field) == "street":
        # start an instance of class Street()...
        move_to_street = streets.Street()
        print("Straßenname: ", move_to_street.allstreets[go_to_field])
        print("Basismiete:", move_to_street.allbaserents[go_to_field])
        print("Miete mit allen Straßen: ", move_to_street.allbaserents_with_all_streets[go_to_field])
        print("Miete mit einem Haus:", move_to_street.allbaserent_with_one_house[go_to_field])
        print("Miete mit zwei Häusern: ", move_to_street.allbaserent_with_two_houses[go_to_field])
        print("Miete mit drei Häusern:", move_to_street.allbaserent_with_three_houses[go_to_field])
        print("Miete mit vier Häusern: ", move_to_street.allbaserent_with_four_houses[go_to_field])
        print("Miete mit einem Hotel:", move_to_street.allbaserent_with_one_hotel[go_to_field])
        # ...check, who the street belongs to...
        # ...pay rent, buy houses, hotels, take mortage...
    
    elif dice.get_field_type(go_to_field) == "community":
        #print("Community!")
        pass
    
    elif dice.get_field_type(go_to_field) == "taxes":
        #print("Taxes!")
        pass
    
    elif dice.get_field_type(go_to_field) == "station":
        #print("Station!")
        pass

    elif dice.get_field_type(go_to_field) == "event":
        #print("Event!")
        pass

    elif dice.get_field_type(go_to_field) == "visiting":
        #print("Visiting!")
        pass

    elif dice.get_field_type(go_to_field) == "plant":
        #print("Plant!")
        pass

    elif dice.get_field_type(go_to_field) == "parking":
        print("Free Parking!")

    """ decision = str(input("Nächster Wurf...[Y/n]"))
    if decision == "Y":
        if doublecheck == 1:
            counter == counter
        elif counter < 3:
            counter += 1
        else:
            counter = 0
    else:
        print("Ende")
        break
         
        # write in json file
        import json
        file = open('/filesave/playername.json', 'w+')
        data = { "x": 12153535.232321, "y": 35234531.232322 }
        json.dump(data, file)
        # https://stackoverflow.com/questions/4450144/easy-save-load-of-data-in-python#4450248
        # load from json file
        import json
        file = open('/usr/data/application/json-dump.json', 'r')
        print json.load(file) """

def main():
    player.add_number_of_players()
    get_player_ready()

main()

    
    
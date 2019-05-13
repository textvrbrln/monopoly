#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import dice
import streets
import player

'''Start event loop'''
def get_player_ready():    
        playerlist_length = len(player.playerlist)
        print("Anzahl der Spieler: ", playerlist_length)
        press = input("Los gehts mit [Enter]...")
        if press == "":
            start_game(playerlist_length)
        else:
            quit()

def start_game(playerlist_length):
        for element in range(0, playerlist_length):
            print("Spieler "+player.playerlist[element]+" würfelt!")
            play(player.playerlist[element])
            decision = input("Nächster Spieler? (y/n)")
            if decision == "y" and (int(playerlist_length)-int(element) == 1):
                #print("Element: "+str(element)+" / Player: "+str(playerlist_length))
                start_game(playerlist_length)
            elif decision == "y" and element < playerlist_length:
                #print("Element: "+str(element)+" / Player: "+str(playerlist_length))
                continue
            else:
                main()

def play(playername):
    spieler = player.Playerclass(playername, 10000)
    print(spieler.name)
    wurf = spieler.throw_dice()
    print(wurf)
    # throw_dice and move to field number X
    # Klasse player
        # playername
            # playerid (einmalig)
        # kontostand
            # zahlen
            # kassieren
        # aktuelles feld
            # würfeln
            # feld wechseln
        # kartenbesitz
            # karte ziehen
            # karte anwenden
            # karte behalten
        # Straßenbesitz
            # mit drei Straßen
            # mit einem Haus
            # ...
            # mit Hypothek
        # Werkbesitz
            # mit einem Werk
        # Bahnhofsbesitz
            # mit einem Bahnhof
            # ...

    # add player profile
    
    go_to_field = spieler.move_forward()
    print(str(playername)+" würfelt eine "+str(wurf))
    print(str(playername)+" landet auf Feld "+str(go_to_field))
    doublecheck = dice.double[0]
    if doublecheck == 1:
        print("Pasch!")
        # a) User plays again
        # b) User goes to Jail
    else:
        pass

    # If move-to-field is a street...
    if dice.get_field_type(go_to_field) == "street":
        # start an instance of class Street()...
        move_to_street = streets.Street()
        print("Straßenname: ", move_to_street.allstreets[go_to_field])
        print("Basismiete:", move_to_street.allbaserents[go_to_field])
        #print("Miete mit allen Straßen: ", move_to_street.allbaserents_with_all_streets[go_to_field])
        #print("Miete mit einem Haus:", move_to_street.allbaserent_with_one_house[go_to_field])
        #print("Miete mit zwei Häusern: ", move_to_street.allbaserent_with_two_houses[go_to_field])
        #print("Miete mit drei Häusern:", move_to_street.allbaserent_with_three_houses[go_to_field])
        #print("Miete mit vier Häusern: ", move_to_street.allbaserent_with_four_houses[go_to_field])
        #print("Miete mit einem Hotel:", move_to_street.allbaserent_with_one_hotel[go_to_field])
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
    # update player profile
    # autosave player profile
    # autosave state

def main_menu():
    print("Willkommen bei Monopoly.")
    print("")
    print("\t\tNeues Spiel starten [n].")
    print("\t\tAltes Spiel laden [l].")
    print("\t\tEinstellungen ändern [e].")
    print("\t\tSpiel fortsetzen [f].")
    print("\t\tSpiel beenden [b].")
    print("")
    choice = input("Wähle eine Option:")
    if choice == "n":
        player.add_number_of_players()
    elif choice == "l":
        pass
    elif choice == "e":
        pass
    elif choice == "f":
        pass
    elif choice == "b":
        quit()

def main():
    main_menu()
    get_player_ready()

main()


"""
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
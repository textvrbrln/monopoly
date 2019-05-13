#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
"""Set up all players"""

player_minimum = 2
player_maximum = 4
player_name_max_length = 12
playerlist =  []
addplayer = []

def add_number_of_players():
        chose_players = input(
                             "Zahl der Spieler "
                             "(["+str(player_minimum)+"] "
                             "bis ["+str(player_maximum)+"]): ")
        # we need to add one player for the range statement
        number_of_players = ((int(chose_players)+1))
        if int(chose_players) < player_minimum:
            print ("Falsche Eingabe")
        elif int(chose_players) > player_maximum:
            print ("Falsche Eingabe")
        else:
            name_players(number_of_players)
        

def name_players(number_of_players):
    for i in list(range(1,number_of_players)):
        addplayer = input(
                         "Bitte wähle einen Namen"
                         " für Spieler "+str(i)+" "
                         "(nur Buchstaben): ")
        if addplayer and len(addplayer) > player_name_max_length:
            print(
                 "Bitte nicht mehr als "
                 ""+str(player_name_max_length)+" "
                 "Buchstaben eingeben.")
            break
        else:
            add_player(addplayer)
            print("Spieler "+str(i)+" heißt "+str(addplayer)+"!")
    
def add_player(addplayer):
    playerlist.append(addplayer)
    return playerlist
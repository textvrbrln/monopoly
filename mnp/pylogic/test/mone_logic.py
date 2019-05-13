#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import player

'''Start event loop'''

def get_player_ready():    
        playerlist_length = len(player.playerlist)
        for elements in list(range(1,playerlist_length)):
                playername = player.playerlist[elements]
                print("Pop:", playername)
                play(playername)
                print("Zurück")

def play(playername):
        # 
        print("Dice")
        print(playername)
        
        """ # write in json file
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
    
    # throw_dice and move to field number X
    #""" decision = str(input("Nächster Wurf...[Y/n]"))
    #if decision == "Y":
    #    if doublecheck == 1:
    #        counter == counter
    #    elif counter < 3:
    #        counter += 1
    #    else:
    #        counter = 0
    #else:
    #    print("Ende")
    #    break """
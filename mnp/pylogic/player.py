#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import random

"""Set up all players"""

player_minimum = 2
player_maximum = 4
first_player = 1
player_name_max_length = 12
playerlist =  []
addplayer = []
onfield = [0]
double = [0]
move_fwd = 0
dice_result = [0]


def add_number_of_players():
        chose_players = input(
                             "Zahl der Spieler "
                             "(["+str(player_minimum)+"] "
                             "bis ["+str(player_maximum)+"]): ")
        check_input(chose_players)
        
def check_input(chose_players):
        try:
            chose_players = int(chose_players)
            evaluate_input(chose_players)
        except ValueError:
            print("Bitte eine Zahl eingeben!")
            add_number_of_players()

def evaluate_input(chose_players):      
        if int(chose_players) < player_minimum:
            print("Zahl zu klein.")
            add_number_of_players()
        elif int(chose_players) > player_maximum:
            print("Zahl zu groß.")
            add_number_of_players()
        else:
            # we need to add one player for the range statement
            number_of_players = ((int(chose_players)+1))
            name_players(number_of_players)
    
def name_players(number_of_players):
    for player in list(range(first_player,number_of_players)):
        add_playernames(player)

def add_playernames(player):
        addplayer = input(
                         "Bitte wähle einen Namen"
                         " für Spieler "+str(player)+" "
                         "(nur Buchstaben): ")
        if addplayer and len(addplayer) > player_name_max_length:
            print(
                 "Bitte nicht mehr als "
                 ""+str(player_name_max_length)+" "
                 "Buchstaben eingeben.")
            add_playernames(int(player))
        else:
            add_player(addplayer)
            print("Spieler "+str(player)+" heißt "+str(addplayer)+"!")

def add_player(addplayer):
    playerlist.append(addplayer)
    return playerlist

class Playerclass:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
    
    def throw_dice(self):
        '''Throw two dice, add result and return'''
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        result_of_dices = ((dice1 + dice2))
        # check for double
        
        if dice1 == dice2:
            double[0] = 1
        else:
            double[0] = 0
        return result_of_dices
    
    def move_forward(self):
        dice_result[0] = Playerclass.throw_dice(self)
        move_fwd = ((onfield[0] + dice_result[0]))
        if move_fwd > 12:
            move_fwd = ((onfield[0] + dice_result[0] - 12))
            onfield[0] = move_fwd
            return move_fwd
        else:
            onfield[0] = move_fwd
            return move_fwd
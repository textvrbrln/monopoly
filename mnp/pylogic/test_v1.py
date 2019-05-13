#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import random
double = [0]
move_fwd = 0
dice_result = [0]
onfield = [0]

playername = ['Hans', 'Franz']

class Playerclass:
    def __init__(self, name, credit, dice, field):
        self.name = name
        self.credit = credit
        self.dice = dice
        self.field = field

    def throw_dice(self):
        dice = random.randrange(1, 7)
        return dice
    
    def move_forward(self, playername, playerdice, playerfield):
        move_fwd = ((playerfield + playerdice))
        if move_fwd > 12:
            move_fwd = ((playerfield + playerdice - 12))
            playerfield = move_fwd
            return playerfield
        else:
            playerfield = move_fwd
            return playerfield

def play(playername):
    player = Playerclass(playername, 0, 0, 0)
    playerdice = player.throw_dice()
    playercredit = 1500
    playerfield = player.move_forward(playername, playerdice, player.field)
    player.field = playerfield
    print("Spieler: "+str(playername)+""
         " würfelt eine "+str(playerdice)+""
         " landet auf Feld "+str(playerfield)+""
         " und verfügt über: "+str(playercredit)+" Monopoly-Dollar.")

for elements in range(0,len(playername)):
    play(playername[elements])
    if elements > len(playername):
        elements = 0

""" def throw_dice(self):
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
        move_fwd = ((playerfield + dice_result[0]))
        if move_fwd > 12:
            move_fwd = ((playerfield + dice_result[0] - 12))
            playerfield = move_fwd
            return move_fwd
        else:
            playerfield = move_fwd
            return move_fwd

for player in range(0,len(playername)):
    spieler = Playerclass(playername[player], 10000)
    print(spieler.name)
    wurf = spieler.throw_dice()
    print(wurf)
    
    go_to_field = spieler.move_forward()
    print(str(spieler.name)+" würfelt eine "+str(wurf))
    print(str(spieler.name)+" landet auf Feld "+str(go_to_field))
    doublecheck = double[0]
    if doublecheck == 1:
        print("Pasch!")
        # a) User plays again
        # b) User goes to Jail
    else:
        pass
 """

""" import player
import dice

playerlist = ["Eins", "Zwo", "Drei", "Vier", "Fünf", "Sechs"]

def get_player_ready():    
        playerlist_length = 6
        print("Anzahl der Spieler: ", playerlist_length)
        print("Los gehts!")
        start_game()

def start_game():
        playerlist_length = 6
        for element in range(0, playerlist_length):
            print("Spieler "+playerlist[element]+" würfelt!")
            # dice
            # If Pasch
                # play(playerlist[element])
                # play again
            # Else
                # play(playerlist[element])

def play(playername): 
    print("Dice")
    print("Kaufen")
    print("Spieler:", playername)
 """
""" def add_players():
        chose_players = input(
                             "Zahl der Spieler "
                             "([2] "
                             "bis [4]): ")
        check_input(chose_players)

def check_input(chose_players):
        try:
            chose_players = int(chose_players)
            evaluate_input(chose_players)
        except ValueError:
            print("Bitte eine Zahl eingeben!")
            add_players()

def evaluate_input(chose_players):
        if int(chose_players) < 2:
            print("Zahl zu klein.")
            add_players()
        elif int(chose_players) > 4:
            print("Zahl zu groß.")
            add_players()

add_players() 
get_player_ready()"""
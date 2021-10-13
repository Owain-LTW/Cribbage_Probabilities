#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:13:24 2021

@author: oltw
"""

import sys
import numpy
import re
from random import sample

def main():
    script = sys.argv[0]
    
    hand1_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands1.csv'
    hand2_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands2.csv'
    crib_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_cribs.csv'
    undealt_cards_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/remaining_cards.csv'
    
    hand1_possibilities = numpy.genfromtxt(hand1_path, dtype = str)
    hand2_possibilities = numpy.genfromtxt(hand2_path, dtype = str)
    crib_possibilities = numpy.genfromtxt(crib_path, dtype = str)
    deck = numpy.genfromtxt(undealt_cards_path, dtype = str)
    
    print('Hand 1',hand1_possibilities)
    #print('Hand 2',hand2_possibilities)
    #print('Crib',crib_possibilities)
    #print('UDC',deck)
    
    cut_card = numpy.random.choice(deck,1)
    
    #print(cut_card)
    
    for hand in range (0,len(hand1_possibilities)):
        calculate_score(hand1_possibilities[hand], cut_card)

def calculate_score(hand, cut_card):
    calc_15s(hand, cut_card)
    #calc_runs(hand, cut_card)#+calc_pairs(hand)+calc_flushes(hand)
    #return(total_score)

def calc_15s(hand, cut_card):
    card_values = [hand[0],hand[3],hand[6],hand[9]]
    #print(card_values)
    #if item in list is J,Q,K,0 then make it 10
    if card_values[0] == 'J' or card_values[0] == 'Q' or card_values[0] == 'K':
        card_values[0] = '10'
    if card_values[1] == 'J' or card_values[1] == 'Q' or card_values[1] == 'K':
        card_values[1] = '10'
    if card_values[2] == 'J' or card_values[2] == 'Q' or card_values[2] == 'K':
        card_values[2] = '10'
    if card_values[3] == 'J' or card_values[3] == 'Q' or card_values[3] == 'K':
        card_values[3] = '10'
    
    card_values = list(map(int, card_values))
    cut_card_value = cut_card[0][0]
    
    if cut_card_value == 'J' or cut_card_value == 'Q' or cut_card_value == 'K':
        cut_card_value = '10'
        
    card_values_cut = card_values.copy()
    card_values_cut.append(int(cut_card_value))
    #add value of cut card to card_values list
    #put minus 1 on len(card_values)
    #then for calculation of 15s score with crib, copy code below, but add extra
    #   loop for 5th card
    
    #score calculation without cut card
    score_no_cut = 0
    for i in range(0,len(card_values)):
        for j in range(0,len(card_values)):
            if j <= i:
                continue
            if card_values[i]+card_values[j]==15:
                score_no_cut = score_no_cut + 2
            for k in range (0,len(card_values)):
                if k <= j:
                    continue
                if card_values[i]+card_values[j]+card_values[k] == 15:
                    score_no_cut = score_no_cut + 2
    if card_values[0] + card_values[1] + card_values[2] + card_values[3] == 15:
        score_no_cut = score_no_cut + 2
    
    score_cut = 0
    for i in range(0,len(card_values_cut)):
        for j in range(0,len(card_values_cut)):
            if j <= i:
                continue
            if card_values_cut[i]+card_values_cut[j]==15:
                score_cut = score_cut + 2
            for k in range (0,len(card_values_cut)):
                if k <= j:
                    continue
                if card_values_cut[i]+card_values_cut[j]+card_values_cut[k] == 15:
                    score_cut = score_cut + 2
                for l in range (0,len(card_values_cut)):
                    if l <= k:
                        continue
                    if card_values_cut[i]+card_values_cut[j]+card_values_cut[k]+card_values_cut[l] == 15:
                        score_cut = score_cut + 2
    if card_values_cut[0] + card_values_cut[1] + card_values_cut[2] + card_values_cut[3] + card_values_cut[4]== 15:
        score_cut = score_cut + 2
    print(card_values, score_no_cut, card_values_cut, score_cut)

#def calc_runs(hand, cut_card):
    #use regex here. Study.
    #if sequence in hand:
    #    print(hand, True)
    #else:
    #    print(hand, False)

if __name__ == '__main__':
   main()


#def calc_runs:
    
#def calc_pairs:
    
#def calc_flushes:
    
 
#Read in all files DONE

#Create an array (look up .dat files)
#Array: hand1  score  hand2  score  hand1+cut  score  liklihood  hand2+cut  score  liklihood

#Calculate score function for hand 1, hand 2 and crib (with and without cut card)

#Without cut card, calculate probability for getting each card value with
#the information available.
#The information is that you know what cards you have in your hand, and you know
#the two cards that have been removed into the crib, and that opponent has 6 cards.





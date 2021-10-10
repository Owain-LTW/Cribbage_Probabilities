#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:13:24 2021

@author: oltw
"""

import sys
import numpy
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
    print('Hand 2',hand2_possibilities)
    print('Crib',crib_possibilities)
    print('UDC',deck)
    
    cut_card = numpy.random.choice(deck,1)
    
    print(cut_card)
    
    for hand in range (0,len(hand1_possibilities)):
        print(hand1_possibilities[hand])
        calculate_score(hand1_possibilities[hand], cut_card)
        


def calculate_score(hand, cut_card):
    total_score = calc_15s(hand, cut_card)#+calc_runs(hand)+calc_pairs(hand)+calc_flushes(hand)
    return(total_score)

def calc_15s(hand, cut_card):
    card_values = [hand[3],hand[9],hand[15],hand[21]]
    #if item in list is J,Q,K,0 then make it 10
    card_values = list(map(int, card_values))
    score = 0
    for i in range(0,len(card_values)):
        if card_values[i] == 'J' or card_values[i] == 'Q' or card_values[i] == 'K':
            card_values[i] = '10'
        for j in range(0,len(card_values)):
            if j <= i:
                continue
            if card_values[i]+card_values[j]==15:
                score = score + 2
            for k in range (0,len(card_values)):
                if k <= j:
                    continue
                if card_values[i]+card_values[j]+card_values[k] == 15:
                    score = score + 2
    if card_values[0] + card_values[1] + card_values[2] + card_values[3] == 15:
        score = score + 2
    
    print(card_values, score)

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





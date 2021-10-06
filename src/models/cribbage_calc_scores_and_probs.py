#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:13:24 2021

@author: oltw
"""

import sys
from random import sample

def main():
    script = sys.argv[0]
    
    hand1_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands1.txt'
    hand2_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands2.txt'
    crib_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_cribs.txt'
    undealt_cards_path = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/remaining_cards.txt'
    
    hand1_possibilities = read_cards(hand1_path)
    hand2_possibilities = read_cards(hand2_path)
    crib_possibilities = read_cards(crib_path)
    undealt_cards = read_cards(undealt_cards_path)
    
    print('Hand 1',hand1_possibilities)
    print('Hand 2',hand2_possibilities)
    print('Crib',crib_possibilities)
    print('UDC',undealt_cards)
    
    undealt_cards = undealt_cards[0]
    cut_card = sample(undealt_cards,1)
    
    print(cut_card)
    
    for hand in range (0,len(hand1_possibilities)):
        calculate_score(hand1_possibilities[hand], cut_card)
    
  
def read_cards(filename):
    f=open(filename, 'r')
    lines = f.readlines()
    f.close()
    for card in range (0,len(lines)):
        lines[card]=lines[card].strip()
    return(lines)


def calculate_score(hand, cut_card):
    total_score = calc_15s(hand, cut_card)#+calc_runs(hand)+calc_pairs(hand)+calc_flushes(hand)
    return(total_score)

def calc_15s(hand, cut_card):
    card_values = [hand[3],hand[9],hand[15],hand[21]]
    #if item in list is J,Q,K,0 then make it 10
    for i in range(0,len(card_values)):
        if card_values[i] == 'J' or card_values[i] == 'Q' or card_values[i] == 'K':
            card_values[i] = '10'
    card_values = list(map(int, card_values))
    
    score = 0
    
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





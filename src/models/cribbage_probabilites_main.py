#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cards read from file (main, read_cards), shuffled and 6 cards dealt to each
player (deal_cards).

Cards are represented by two characters; first character is suit (H,D,S,C) and
value (1,2,3,4,5,6,7,8,9,0,J,Q,K). 1 is ace, 0 is 10, J,Q,K are jack, queen, king.
"""

import sys
import numpy
from random import seed
from random import sample

def main():
    script = sys.argv[0]

    file_path = '/Users/oltw/Documents/Cribbage_Probabilities/data/raw/french_cards.txt'
    read_cards(file_path)

def read_cards(filename):
    f=open(filename, 'r')
    lines = f.readlines()
    f.close()
    for card in range (0,52):
        lines[card]=lines[card].strip()
    deal_cards(lines)

def deal_cards(card_list):
    shuffled_deck = sample(card_list,52)
    player1_hand = shuffled_deck[0:6]
    player2_hand = shuffled_deck[6:12]
    remaining_cards = shuffled_deck[12:-1]
    print('Shuffled deck', shuffled_deck)
    print('Player 1', player1_hand)
    print('Player 2', player2_hand)
    print('Remaining Cards', remaining_cards)
    hand_possibilities(player1_hand)
    
def hand_possibilities(hand):
    
    
    for i in range (0,6):
        for j in range (i,6):
            if i == j: continue
            dum_hand = hand.copy()
            dum_hand.remove(hand[i])
            dum_hand.remove(hand[j])
            print('Hand following discarding of 2 cards', dum_hand)
if __name__ == '__main__':
   main()
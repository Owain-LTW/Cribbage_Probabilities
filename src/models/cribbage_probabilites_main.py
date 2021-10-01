#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

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
    deal_cards(lines)

def deal_cards(card_list):
    shuffled_deck= sample(card_list,52)
    player1_hand = shuffled_deck[0:6]
    player2_hand = shuffled_deck[6:12]
    remaining_cards = shuffled_deck[12:-1]
    print('Shuffled deck', shuffled_deck)
    print('Player 1', player1_hand)
    print('Player 2', player2_hand)
    print('Remaining Cards', remaining_cards)
    
if __name__ == '__main__':
   main()
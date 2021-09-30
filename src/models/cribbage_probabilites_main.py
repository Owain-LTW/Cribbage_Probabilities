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
    hands_and_cut = sample(card_list,52)
    player1_hand = hands_and_cut[0:6]
    player2_hand = hands_and_cut[6:12]
    cut_card = hands_and_cut[-1]
    remaining_cards = hands_and_cut[12:-2]
    print('Hands and cut',hands_and_cut)
    print(player1_hand)
    print(player2_hand)
    print(cut_card)
    print(remaining_cards)
    
if __name__ == '__main__':
   main()
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
from random import sample
from random import shuffle

def main():
    script = sys.argv[0]

    file_path = '/Users/oltw/Documents/Cribbage_Probabilities/data/raw/french_cards.csv'
    cards = numpy.loadtxt(file_path,delimiter = ',', dtype = str)
    
    deal_cards(cards)

def deal_cards(cards):
    numpy.random.shuffle(cards)   
    player1_hand = cards[0:6]
    player2_hand = cards[6:12]
    remaining_cards = cards[12:-1]
    #print('Shuffled deck', cards)
    #print('Player 1', player1_hand)
    #print('Player 2', player2_hand)
    #print('Remaining Cards', remaining_cards)
    hand_possibilities(player1_hand, player2_hand, remaining_cards)
    
def hand_possibilities(hand1, hand2, remaining_cards):
    file_path1 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands1.csv'
    file_path2 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands2.csv'
    file_path3 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_cribs.csv'
    file_path4 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/remaining_cards.csv'
    
    possible_hands1 = numpy.empty((0,4), dtype = 'str')
    possible_hands2 = numpy.empty((0,4), dtype = 'str')
    possible_cribs = numpy.empty((0,4), dtype = 'str')
    
    for i in range (0,6):
        for j in range (i,6):
            if i == j: continue
            dum_hand1 = hand1.copy()
            dum_hand2 = hand2.copy()
            
            dum_hand1 = numpy.delete(dum_hand1, [i,j])

            dum_hand2 = numpy.delete(dum_hand2, [i,j])
                      
            #print(dum_hand1)
            
            crib = hand1[i],hand1[j],hand2[i],hand2[j]
            
            possible_hands1 = numpy.append(possible_hands1, [dum_hand1], axis = 0)
            possible_hands2 = numpy.append(possible_hands2, [dum_hand2], axis = 0)
            possible_cribs = numpy.append(possible_cribs, [crib], axis = 0)
            
            print(dum_hand1)
            print(possible_hands1)
            
    numpy.savetxt(file_path1, possible_hands1, fmt='%2s', delimiter = ',')
    numpy.savetxt(file_path2, possible_hands2, fmt='%2s', delimiter = ',')
    numpy.savetxt(file_path3, possible_cribs, fmt='%2s', delimiter = ',')
    
    numpy.savetxt(file_path4, [remaining_cards], fmt='%2s', delimiter = ',')
    
if __name__ == '__main__':
   main()
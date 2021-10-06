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

    file_path = '/Users/oltw/Documents/Cribbage_Probabilities/data/raw/french_cards.dat'
    cards = numpy.loadtxt(file_path,delimiter = ',', dtype = str)
    
    deal_cards(cards)

def deal_cards(cards):
    numpy.random.shuffle(cards)   
    player1_hand = cards[0:6]
    player2_hand = cards[6:12]
    remaining_cards = cards[12:-1]
    print('Shuffled deck', cards)
    print('Player 1', player1_hand)
    print('Player 2', player2_hand)
    print('Remaining Cards', remaining_cards)
    hand_possibilities(player1_hand, player2_hand, remaining_cards)
    
def hand_possibilities(hand1, hand2, remaining_cards):
    file_path1 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands1.dat'
    file_path2 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_hands2.dat'
    file_path3 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/possible_cribs.dat'
    file_path4 = '/Users/oltw/Documents/Cribbage_Probabilities/src/data/remaining_cards.dat'
    f1=open(file_path1,'w')
    f2=open(file_path2,'w')
    f3=open(file_path3,'w')
    f4=open(file_path4,'w')
    for i in range (0,6):
        for j in range (i,6):
            if i == j: continue
            dum_hand1 = hand1.copy()
            dum_hand2 = hand2.copy()
            
            dum_hand1.remove(hand1[i])
            dum_hand1.remove(hand1[j])
            
            dum_hand2.remove(hand2[i])
            dum_hand2.remove(hand2[j])
            
            crib = hand1[i],hand1[j],hand2[i],hand2[j]
            crib = list(crib)
            #print('Hand 1 following discarding of 2 cards', dum_hand1)
            #print('Hand 2 following discarding of 2 cards', dum_hand2)
            f1.write(str(dum_hand1)+'\n')
            f2.write(str(dum_hand2)+'\n')   
            f3.write(str(crib)+'\n')
    
    f4.write(str(remaining_cards))
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    
if __name__ == '__main__':
   main()
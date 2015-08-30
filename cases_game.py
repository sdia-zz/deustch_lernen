#!/usr/bin/env python
#-*- coding:utf-8 -*-


import random


CASES = dict(
    Nom = {'Mas.': 'der',
           'Neu.': 'das',
           'Fem.': 'die',
           'Plu.': 'die'},
    
    Akk = {'Mas.': 'den',
           'Neu.': 'das',
           'Fem.': 'die',
           'Plu.': 'die'},
    
    Dat = {'Mas.': 'dem',
           'Neu.': 'dem',
           'Fem.': 'der',
           'Plu.': 'den'},

    Gen = {'Mas.': 'des',
           'Neu.': 'des',
           'Fem.': 'der',
           'Plu.': 'der'})


if __name__ == '__main__':
    while True:
        case = random.choice(CASES.keys())
        gen = random.choice(CASES[case].keys())
        art = CASES[case][gen]
        try:
            print '-' * 80
            print '{}, {}:'.format(gen, case)
            res = raw_input('Your answer:')
            while res != art:
                res = raw_input('try again:')
            print 'OK'
        except KeyboardInterrupt:
            print '\n\t\t\t\tBye.'
            exit()

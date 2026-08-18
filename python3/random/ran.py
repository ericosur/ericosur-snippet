#!/usr/bin/env python3
#
''' just pick one name from name list randomly '''

import argparse
import random

from random_common import do_nothing, get_logd, prt

logd = do_nothing
NAME_LIST = ('alice', 'bob', 'cathy', 'david', 'eric',
             'fred', 'grace', 'helen', 'iris', 'jacob',
             'keem', 'liam', 'mills', 'nick', 'oliver')

ADJ_LIST = ('happy', 'sad', 'angry', 'funny', 'serious',
            'smart', 'dumb', 'rich', 'poor', 'tall',
            'short', 'fat', 'thin', 'strong', 'weak',
            'brave', 'lazy', 'kind', 'loud', 'young')


class RandomDemo:
    """Generate random name and adjective combinations."""
    
    def __init__(self, repeat: int = 4):
        """Initialize RandomDemo instance.
        
        Args:
            repeat: Number of times to generate random pairs (default: 4)
        """
        self.repeat = repeat
    
    def run(self):
        """Run the demo to generate random name and adjective pairs."""
        name_size = len(NAME_LIST)
        logd(f'name_size: {name_size}')
        adj_size = len(ADJ_LIST)
        logd(f'adj_size: {adj_size}')

        for i in range(self.repeat):
            idx = random.randint(0, name_size - 1)
            logd(f'picked idx for name_list: {idx}')
            choice_idx = random.randrange(len(ADJ_LIST))
            logd(f'picked idx for adj_list: {choice_idx}')

            prt(f'{i:02d}: {ADJ_LIST[choice_idx]} {NAME_LIST[idx]}')


def demo(repeat: int = 4):
    '''demo function'''
    RandomDemo(repeat).run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pick random names and adjectives')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug logging')
    parser.add_argument('-n', '--number', type=int, default=4, help='number of random pairs to generate (default: 4)')
    args = parser.parse_args()
    
    if args.debug:
        logd = get_logd()
    else:
        logd = do_nothing
    
    demo(args.number)

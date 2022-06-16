"""

Created by GrandEchoWhiskey.

https://github.com/GrandEchoWhiskey

Blood type probability.

"""
from util import *

from classes import *

def main():
    parent1 = Person(formatInput(input('Parent 1 bloodtype: ')))
    parent2 = Person(formatInput(input('Parent 2 bloodtype: ')))

    print(parent1)
    print(parent2)

if __name__ == '__main__':
    main()
"""

Created by GrandEchoWhiskey.

https://github.com/GrandEchoWhiskey

Blood type probability.

"""

from util import *

BLOOD_TRAIT = ['A', 'B', '0']
RH_TRAIT = ['+', '-']

RECESIVE_PROBS = 2/3

def formatInput(string: str):
    blood: str = ''
    rh: str = ''
    possible_blood: list = [x + y for x in BLOOD_TRAIT for y in BLOOD_TRAIT] + BLOOD_TRAIT
    possible_rh: list = [x + y for x in RH_TRAIT for y in RH_TRAIT] + RH_TRAIT
    for bloodtype in possible_blood:
        if string.find(bloodtype) != -1:
            blood = bloodtype.sorted()
            blood = blood[::-1] if tmp[0] == '0' else blood
            blood = 'AB' if blood == 'BA' else blood
            break
        elif bloodtype == '0':
            return None

    for rhtype in possible_rh:
        if string.find(rhtype) != -1:
            rh = rhtype.sorted()
            break
        elif rhtype == '-':
            return None

    return blood, rh


def main():
    parent1 = formatInput(input('Parent 1 bloodtype: '))
    parent2 = formatInput(input('Parent 2 bloodtype: '))

if __name__ == '__main__':
    main()
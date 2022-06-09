"""

Created by GrandEchoWhiskey.

https://github.com/GrandEchoWhiskey

Blood type probability.

"""

# Only accepted types
BLOOD = ['AB', 'AA', 'BB', 'A0', 'B0', '00', 'A', 'B', '0']
RH = ['++', '+-', '--', '+', '-']

RECESIVE_PROBS = 2/3

class Allele:
    def __init__(self, a1, a2, prob=1):
        self.a1 = a1
        self.a2 = a2
        self.prob = prob

class Person:
    def __init__(self, blood, rh):

        self.blood = self.formatAlleles(blood, '0')
        self.rh = self.formatAlleles(rh, '-')

    def formatAlleles(self, alleles, recesive):

        if len(alleles) == 2:
            return [Allele(alleles[:1:], alleles[1::])]

        if len(alleles) == 1 and alleles != recesive:
            return [Allele(alleles, alleles, 1-RECESIVE_PROBS), Allele(alleles, recesive, RECESIVE_PROBS)]

        return [Allele(recesive, recesive)]

    def combination(self, other):

        blood_res = list()
        rh_res = list()

        for item_1 in self.blood:
            for item_2 in other.blood:
                prob = item_1.prob * item_2.prob
                blood_res.extend([
                    Allele(item_1.a1, item_2.a1, prob), Allele(item_1.a1, item_2.a2, prob),
                    Allele(item_1.a2, item_2.a1, prob), Allele(item_1.a2, item_2.a2, prob)
                ])

        for item_1 in self.rh:
            for item_2 in other.rh:
                prob = item_1.prob * item_2.prob
                rh_res.extend([
                    Allele(item_1.a1, item_2.a1, prob), Allele(item_1.a1, item_2.a2, prob),
                    Allele(item_1.a2, item_2.a1, prob), Allele(item_1.a2, item_2.a2, prob)
                ])

        res = list()
        for item_1 in blood_res:
            for item_2 in rh_res:
                res.append([str(item_1.a1)+str(item_1.a2)+str(item_2.a1)+str(item_2.a2), item_1.prob * item_2.prob])

        return res

def sortData(data):
    sort = dict()
    for item in data:

        blood = item[0][:2:]

        if blood == 'BA':
            blood = 'AB'

        if blood == '0A':
            blood = 'A0'

        if blood == '0B':
            blood = 'B0'

        rh = item[0][2::]
        if rh == '-+':
            rh = '+-'

        if blood+rh not in sort.keys():
            sort[blood+rh] = 0

        sort[blood+rh] = sort[blood+rh] + item[1]

    avg_s = 0
    for key in sort:
        avg_s = avg_s + sort[key]

    for key in sort:
        sort[key] = sort[key] / avg_s

    return sort

def formatType(type):

    bloodType = '0'
    for bType in BLOOD:
        finder = type.find(bType)
        if finder != -1:
            bloodType = type[finder:finder + len(bType)]
            break

    rhType = '+'
    for rhType in RH:
        finder = type.find(rhType)
        if finder != -1:
            rhType = type[finder:finder + len(rhType)]
            break

    return bloodType, rhType

def getBlood(blood):
    match(blood):
        case 'AB':
            return 'AB'
        case 'AA' | 'A0':
            return 'A'
        case 'BB' | 'B0':
            return 'B'
    return '0'

def getRh(rh):
    """
    Rh- is recesive, so only two '-' alleles can
    result in negative Rh. One '+' just becomes dominant.
    """
    if rh == '--':
        return '-'
    return '+'

def shortenData(data):
    nData = dict()
    for key in data:
        newName = getBlood(key[:2:])+getRh(key[2::])
        if newName not in nData.keys():
            nData[newName] = 0
        nData[newName] = nData[newName] + data[key]
    return nData


def main():

    bloodtype = input('Your fathers blood type: ')
    blood, rh = formatType(bloodtype)
    father = Person(blood, rh)

    bloodtype = input('Your mothers blood type: ')
    blood, rh = formatType(bloodtype)
    mother = Person(blood, rh)

    child = father.combination(mother)

    printer = shortenData(sortData(child))

    newPri = {k: v for k, v in sorted(printer.items(), key=lambda item: item[1], reverse=True)}
    for key in newPri:
        print(key + ": " + str(round(newPri[key]*100, 2)) + "%")

if __name__ == '__main__':
    main()


from classes import BLOOD_TRAIT, RH_TRAIT

def formatInput(string: str):
    string = string.upper()
    blood: str = ''
    rh: str = ''
    possible_blood: list = [x + y for x in BLOOD_TRAIT for y in BLOOD_TRAIT] + BLOOD_TRAIT
    possible_rh: list = [x + y for x in RH_TRAIT for y in RH_TRAIT] + RH_TRAIT
    for bloodtype in possible_blood:
        if string.find(bloodtype) != -1:
            blood_l = [s for s in bloodtype]
            blood_l.sort()
            blood = ''.join(blood_l)
            blood = blood[::-1] if blood[0] == '0' else blood
            blood = 'AB' if blood == 'BA' else blood
            break
        elif bloodtype == '0':
            return None

    for rhtype in possible_rh:
        if string.find(rhtype) != -1:
            rh_l = [s for s in rhtype]
            rh_l.sort()
            rh = ''.join(rh_l)
            break
        elif rhtype == '-':
            return None

    return blood + rh
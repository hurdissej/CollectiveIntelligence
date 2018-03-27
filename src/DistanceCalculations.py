from math import sqrt, pow

def euc_distance(prefs, person1, person2):
    si = []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)

    if len(si) == 0: return 0

    sum_of_squares = 0
    for film in si:
        sum_of_squares += pow(prefs[person1][film] - prefs[person2][film],2)

    return 1/(1+sqrt(sum_of_squares))

def pearson(prefs, person1, person2):
    si = []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)

    n = len(si)

    if n ==0: return 0
    sumPerson1 = sum([prefs[person1][film] for film in si])
    sumPerson2 = sum([prefs[person2][film] for film in si])

    sumPerson1Sq = sum([pow(prefs[person1][film],2) for film in si])
    sumPerson2Sq = sum([pow(prefs[person2][film], 2) for film in si])

    pSum = sum([prefs[person1][film] * prefs[person2][film] for film in si])

    num = pSum-(sumPerson1*sumPerson2/n)
    den = sqrt((sumPerson1Sq-pow(sumPerson1,2)/n)*( sumPerson2Sq - pow(sumPerson2,2)/n))
    if den == 0: return 0
    return num/den
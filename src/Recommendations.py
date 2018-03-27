from DistanceCalculations import pearson

def loadMovieLens(path='C:\Code\ProgrammingCollectiveIntelligence\src\data'):
  # Get movie titles
    movies = {}
    for line in open(path + '/movies.csv', encoding="utf8"):
        (id, title) = line.split(',')[0:2]
        movies[id] = title
  # Load data
    prefs = {}
    for line in open(path + '/ratings.csv', encoding="utf8"):
        (user, movieid, rating, ts) = line.split(',')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs


def topMatches(prefs, person, n=5, similarity=pearson):
    scores = []
    for other in prefs:
        if other != person:
            scores.append((similarity(prefs, person, other), other))
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity=pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        if other != person:
            sim = similarity(prefs, person, other)

            if sim > 0:
                for film in prefs[other]:
                    if film not in prefs[person]:
                        totals.setdefault(film, 0)
                        totals[film] += prefs[other][film] * sim
                        simSums.setdefault(film, 0)
                        simSums[film] += sim

    rankings = [(total / simSums[film], film) for film, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result[item][person] = prefs[person][item]

    return  result
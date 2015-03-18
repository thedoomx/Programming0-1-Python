def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)

    result = 0

    index = 0

    while index < len(beers):
        result += beers[index] * fries[index]

        index += 1

    return result

import shapes


def filterx(predicate, values):
    matchingValues = []
    for value in values:
        if predicate(value):
            matchingValues.append(value)

    return matchingValues

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    matchingValues = filterx(lambda x: x % 2 == 0, values)
    print(matchingValues)


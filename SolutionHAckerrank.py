#!/bin/python3

import itertools


def maximumClusterQuality(speed, reliability, maxMachines, speed_count):
    output = []
    speedCombinationSums = []
    speedsSplit = []
    reliabilityCombs = []
    minReliabilities = []

    for i in range(speed_count):
        output.append(speed[i] * reliability[i])

    for i in range(2, maxMachines + 1):
        speedCombinationSums.append([sum(x) for x in itertools.permutations(speed, i)])

    for x in speedCombinationSums:
        for y in x:
            speedsSplit.append(y)

    for i in range(2, maxMachines + 1):
        reliabilityCombs.append([x for x in itertools.permutations(reliability, i)])

    for x in reliabilityCombs:
        for y in x:
            minReliabilities.append(min(y))

    for i in range(len(speedsSplit)):
        output.append(speedsSplit[i] * minReliabilities[i])

    return max(output)


if __name__ == '__main__':
    speed_count = int(input().strip())

    speed = []

    for _ in range(speed_count):
        speed_item = int(input().strip())
        speed.append(speed_item)

    reliability_count = int(input().strip())

    reliability = []

    for _ in range(reliability_count):
        reliability_item = int(input().strip())
        reliability.append(reliability_item)

    maxMachines = int(input().strip())

    print(maximumClusterQuality(speed, reliability, maxMachines, speed_count))

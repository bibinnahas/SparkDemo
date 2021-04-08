def n_length_combo(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)

    return l


# Driver code
if __name__ == "__main__":
    output = []
    all_speed_sums = []
    all_reliability_mins = []

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

    # speed_count = 5
    # speed = [12, 112, 100, 13, 55]
    # reliability = [31, 4, 100, 55, 50]
    # maxMachines = 3

    for i in range(speed_count):
        output.append(speed[i] * reliability[i])

    for i in range(2, maxMachines + 1):
        combination_of_speed = n_length_combo([x for x in speed], maxMachines)
        for i in combination_of_speed:
            all_speed_sums.append(sum(i))
        combination_of_reliability = n_length_combo([x for x in reliability], maxMachines)
        for j in combination_of_reliability:
            all_reliability_mins.append(min(j))

    for i, j in zip(all_speed_sums, all_reliability_mins):
        output.append(i * j)

    # print(combination_of_reliability)
    # print(combination_of_speed)
    #
    # print(all_speed_sums)
    # print(all_reliability_mins)

    print(max(output))





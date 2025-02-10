import itertools
import math
import random

# Deterministicky
def boat_brute_force(space: list):
    perms = list(itertools.permutations(space))
    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) < best:
            best = abs(perm[0] - perm[len(perm) - 1])

    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) == best:
            results.append(perm)

    return results

# Nedeterministicky
def boat_monte_carlo(space: list):
    perms = list()
    while True:
        perm = space[:]
        random.shuffle(perm)
        if perm not in perms:
            perms.append(perm)
        if len(perms) >= 4:
            break

    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) < best:
            best = abs(perm[0] - perm[len(perm) - 1])

    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) == best:
            results.append(perm)

    return results


# Deterministicky
def boat_heuristic(space: list):
    perms = space[:]

    for i in range(0, len(perms)):
        perms.append([c, a, b])
        perms.append([a, b, c])
        perms.append([b, c, a])

    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) < best:
            best = abs(perm[0] - perm[len(perm) - 1])

    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) == best:
            results.append(perm)

    second_result = list(results[0])
    second_result.reverse()
    results.append(second_result)

    return results


if __name__ == "__main__":
    boat: list = [73, 85, 81, 34, 75]
    print("Brute force: " + str(boat_brute_force(boat)))
    print("Monte carlo: " + str(boat_monte_carlo(boat)))
    # print("Heuristic: " + str(boat_heuristic(73, 85, 81)))
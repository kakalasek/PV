import itertools
import math
import random

# Deterministicky
def boat_brute_force(a, b, c):
    perms = list(itertools.permutations([a, b, c]))
    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[2]) < best:
            best = abs(perm[0] - perm[2])

    for perm in perms:
        if abs(perm[0] - perm[2]) == best:
            results.append(perm)

    return results

# Nedeterministicky
def boat_monte_carlo(a, b, c):
    perms = list()
    while True:
        perm = [a, b, c]
        random.shuffle(perm)
        if perm not in perms:
            perms.append(perm)
        if len(perms) >= 4:
            break

    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[2]) < best:
            best = abs(perm[0] - perm[2])

    for perm in perms:
        if abs(perm[0] - perm[2]) == best:
            results.append(perm)

    return results


# Deterministicky
def boat_heuristic(a, b, c):
    perms = list()
    perms.append([c, a, b])    
    perms.append([a, b, c])    
    perms.append([b, c, a])    
    
    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[2]) < best:
            best = abs(perm[0] - perm[2])

    for perm in perms:
        if abs(perm[0] - perm[2]) == best:
            results.append(perm)

    second_result = list(results[0])
    second_result.reverse()
    results.append(second_result)

    return results


if __name__ == "__main__":
    print("Brute force: " + str(boat_brute_force(73, 85, 81)))
    print("Monte carlo: " + str(boat_monte_carlo(73, 85, 81)))
    print("Heuristic: " + str(boat_heuristic(73, 85, 81)))
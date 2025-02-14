import itertools
import math
import random
import tracemalloc
import time

# Deterministicky
def boat_brute_force(space: list):
    tracemalloc.start()
    startTime = time.time()

    # === Zacatek Mereni === 


    perms = list(itertools.permutations(space))
    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) < best:
            best = abs(perm[0] - perm[len(perm) - 1])

    for perm in perms:
        if abs(perm[0] - perm[len(perm) - 1]) == best:
            results.append(perm)
    
    # === Konec Mereni ===

    timeConsumption = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("BRUTE FORCE - Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("BRUTE FORCE - Spotreba casu: " + str(timeConsumption))

    return results

# Nedeterministicky
def boat_monte_carlo(space: list):
    tracemalloc.start()
    startTime = time.time()

    # === Zacatek Mereni === 


    perms = list()
    while True:
        perm = space[:]
        random.shuffle(perm)
        if perm not in perms:
            if len(space) == 1:
                perms.append(perm)
                break
            if len(space) == 2:
                perms.append(space)
                space.reverse()
                perms.append(space)
                break
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

    # === Konec Mereni ===

    timeConsumption = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("MONTE CARLO - Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("MONTE CARLO - Spotreba casu: " + str(timeConsumption))

    return results


# Deterministicky
def boat_heuristic(space: list):
    tracemalloc.start()
    startTime = time.time()

    # === Zacatek Mereni === 

    perms = space[:]

    for i in range(0, len(perms)):
        for i in range(1, len(perms)):
            print(i)

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
    
    # === Konec Mereni ===

    timeConsumption = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("HEURISTIC - Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("HEURISTIC - Spotreba casu: " + str(timeConsumption))

    return results


if __name__ == "__main__":
    boat: list = [73, 85, 95, 81, 36, 76]
    #print("Brute force: " + str(boat_brute_force(boat)))
    print("Monte carlo: " + str(boat_monte_carlo(boat)))
    # print("Heuristic: " + str(boat_heuristic(73, 85, 81)))
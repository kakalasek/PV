import itertools
import math
import random
import time
import tracemalloc

# Deterministicky
def boat_brute_force(a, b, c):
    tracemalloc.start()
    startTime = time.time()

    # === Zacatek Mereni === 

    perms = list(itertools.permutations([a, b, c]))
    best = math.inf
    results = list()
    for perm in perms:
        if abs(perm[0] - perm[2]) < best:
            best = abs(perm[0] - perm[2])

    for perm in perms:
        if abs(perm[0] - perm[2]) == best:
            results.append(perm)

    # === Konec Mereni ===

    timeConsumption = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("BRUTE FORCE - Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("BRUTE FORCE - Spotreba casu: " + str(timeConsumption))

    return results

# Nedeterministicky
def boat_monte_carlo(a, b, c):
    tracemalloc.start()
    startTime = time.time()

    # === Zacatek Mereni === 

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

    # === Konec Mereni ===

    timeConsumption = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("MONTE CARLO - Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("MONTE CARLO - Spotreba casu: " + str(timeConsumption) + " milisec")

    return results


# Deterministicky
def boat_heuristic(a, b, c):
    tracemalloc.start()
    startTime = time.time()

    # === Zacatek Mereni === 

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
    
    # === Konec Mereni ===

    timeConsumption = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("HEURISTIKA - Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("HEURISTIKA - Spotreba casu: " + str(timeConsumption) + " milisec")

    return results


if __name__ == "__main__":
    print("Brute force: " + str(boat_brute_force(73, 85, 81)))
    print("Monte carlo: " + str(boat_monte_carlo(73, 85, 81)))
    print("Heuristic: " + str(boat_heuristic(73, 85, 81)))
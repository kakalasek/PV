import itertools

perms = [78, 69, 106, 140]
n = len(perms)

for i in range(0, n):
    for j in range(i+1, n):
        perm = [None]*n
        perm[0] = perms[i]
        perm[n-1] = perms[j]
        for p in itertools.permutations(perm[1:n]):
            for t in range(1, n-1):
                perm[t] = p[t-1]
            print(perm)
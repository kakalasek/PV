graph = {
    0: [1, 2],
    1: [0],
    2: [0, 3],
    3: [2, 4, 7],
    4: [3, 6, 5],
    5: [4],
    6: [4],
    7: [3],
}

mapping = {
    0:  {"name": "litomerice", "confluence": {"in": "ohre", "out": "labe"}},
    1:  {"name": "smrciny", "river": "ohre"},
    2:  {"name": "melnik", "confluence": {"in": "vltava", "out": "labe"}},
    3:  {"name": "lazne tousen", "confluence": {"in": "jizera", "out": "labe"}},
    4:  {"name": "hradec kralove", "confluence": {"in": "orlice", "out": "labe"}},
    5:  {"name": "orlicke hory", "river": "orlice"},
    6:  {"name": "krkonose", "river": "labe"},
    7:  {"name": "jizerske hory", "river": "jizera"}
}


def perform_mapping(map: dict, path: list) -> list:
    mapped_path = []

    for point in path:
        mapped_path.append(map[point])

    return mapped_path

def reverse_mapping(map: dict, value: str) -> int:
    for k,v in map.items():
        if v['name'] == value:
            return k

def inorder_traversal(v, d, traversed: list, path: list):
    if v in traversed or d in traversed:
        return

    path.append(v)
    traversed.append(v)

    for point in graph[v]:
        inorder_traversal(point, d, traversed, path)

    if d not in traversed:
        path.pop()

point_a = input("Zvolte místo A: ")
point_b = input("Zvolte místo B: ")
point_a = point_a.lower().strip()
point_b = point_b.lower().strip()

point_a = reverse_mapping(mapping, point_a)
point_b = reverse_mapping(mapping, point_b)

path = []

inorder_traversal(point_a, point_b, [], path) 

path = perform_mapping(mapping, path)


print(f"Z {path[0]['name']}")
print(f"Po ", end='')
if 'river' in path[0].keys():
    print(path[0]['river'])
else:
    print(path[0]['confluence']['out'])

print()

for point in path[1:]:
    print(f"Do {point['name']}")

    if 'river' in point.keys():
        print(f"Po {point['river']}")
    else:
        print(f"Po {point['confluence']['out']}")

    print()
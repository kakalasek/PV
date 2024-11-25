vysledky = [
    ("Karel", 31),
    ("Petr", 10),
    ("Honza", 52),
    ("Eva", 61),
    ("Katka", 0),
]

sort_by_points = lambda x: x[1]

print(sorted(vysledky, key=sort_by_points))
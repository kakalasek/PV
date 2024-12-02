rivers = [
    {
        "name": "vltava",
        "spring": "šumava",
        "towns": [
            "praha",
            "český krumlov",
            "české budějovice"
        ]
    },
    {
        "name": "ohře",
        "spring": "smrčiny",
        "towns": [
            "karlovy vary",
            "cheb",
            "sokolov"
        ]
    },
    {
        "name": "jizera",
        "spring": "jizerské hory",
        "towns": [
            "malá skála",
            "bakov nad jizerou",
            "benátky nad jizerou"
        ]
    }
]

everything_worked = 0

user_input = input("Zadejte název města, nebo řeky: ")
user_input = user_input.lower().strip()

for river in rivers:
    if river["name"] == user_input:
        print(f"Pramen reky se nachází v: {river["spring"]}")
        print(f"A proteka temito mesty: ")
        for town in river["towns"]:
            print(town)
        
        everything_worked = 1
        break

    if user_input in river["towns"]:
        print("Mestem protekaji tyto reky: ")
        for river_embedded in rivers:
            if user_input in river_embedded["towns"]:
                print(river_embedded["name"])
        
        everything_worked = 1
        break

if not everything_worked:
    print("Nebyl nalezen žádný záznam pro váš dotaz")
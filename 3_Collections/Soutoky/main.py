rivers = [
    {
        "name": "labe",
        "spring": "krkonoše",
        "confluence_place": "",
        "confluence_river": ""
    },
    {
        "name": "jizera",
        "spring": "jizerské hory",
        "confluence_place": "lázně toušeň",
        "confluence_river": "labe"
    },
    {
        "name": "vltava",
        "spring": "šumava",
        "confluence_place": "mělník",
        "confluence_river": "labe"
    },
    {
        "name": "berounka",
        "spring": "",
        "confluence_place": "praha-zbraslav",
        "confluence_river": "vltava"
    },
    {
        "name": "ohře",
        "spring": "smrčiny",
        "confluence_place": "litoměřice",
        "confluence_river": "labe"
    },
    {
        "name": "teplá",
        "spring": "zádub-zavišín",
        "confluence_place": "karlovy vary",
        "confluence_river": "ohře"
    }
]

user_input = input("Zadejte řeku: ")
user_input = user_input.lower().strip()

inflows = []
flows_to = ""

for river in rivers:
    if river["confluence_river"] == user_input:
        inflows.append(river["name"])
    
    if river["name"] == user_input:
        flows_to = river["confluence_river"]

if not inflows and not flows_to:
    print("Nebyl nalezen žádný záznam pro váš dotaz")
else:
    print(f"Přítoky: {inflows}")
    print(f"Vlévá se do: {flows_to}")
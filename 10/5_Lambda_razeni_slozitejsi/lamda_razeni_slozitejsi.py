zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]

cena_vzestupne = lambda x: x["price"]
nazev_sestupne = lambda x: x["name"]
kategorie_poradi_vzestupne = lambda x: x["cathegory"][0]

# print(sorted(zbozi, key=cena_vzestupne, reverse=True))
# print(sorted(zbozi, key=nazev_sestupne, reverse=True))
print(sorted(zbozi, key=kategorie_poradi_vzestupne))
towns = {"liberec": "liberecký kraj", "karlovy vary": "karlovarský kraj", "česká lípa": "liberecký kraj", "mělník": "středočeský kraj", "příbram": "středočeský kraj"}

user_input = input("Zadejte kraj, nebo město: ")
user_input = user_input.lower()

everything_worked = 0

for town, country in towns.items():
    if user_input == town:
        print(f"Kraj, ve kterém toto město leží jest: {country}")
        everything_worked = 1
        break

    if user_input == country:
        print(f"Tumuto kraji náleží tyto města: ")
        for town_embedded, country_embedded in towns.items():
            if country_embedded == country:
                print(town_embedded)

        everything_worked = 1
        break

if not everything_worked:
    print("No match was found for your request. Make sure you typed everything correctly")
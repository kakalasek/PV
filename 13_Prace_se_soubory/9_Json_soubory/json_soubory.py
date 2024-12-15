import json
import os

def save_json(company_name, ico, phones, desc):
    json_data = []

    with open("company.json", "r+") as jsonfile:
        if not os.stat("company.json").st_size == 0:
            json_data = json.load(jsonfile)

        json_object = {
            "company_name": company_name,
            "ico": ico,
            "phones": phones,
            "desc": desc
        }

        json_data.append(json_object)

        jsonfile.seek(0)

        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    save_json("SPSE Jecna", 61385301, ["224941469","224942066"], """Škola nabízí obory: 
    - Informatika
    - Elektrotechnika
    a její ředitel říka: "Je to nejlepší škola v Praze".
    """)

    save_json("Seznam.cz", 26168685, "234694111", None)

    save_json("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond.")
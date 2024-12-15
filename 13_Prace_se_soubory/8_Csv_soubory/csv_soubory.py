import csv

def save_csv(company_name, ico, phones, desc):
    with open("company.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([company_name, ico, phones, desc])

if __name__ == "__main__":
    save_csv("SPSE Jecna", 61385301, ["224941469","224942066"], """Škola nabízí obory: 
    - Informatika
    - Elektrotechnika
    a její ředitel říka: "Je to nejlepší škola v Praze".
    """)

    save_csv("Seznam.cz", 26168685, "234694111", None)

    save_csv("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond.")
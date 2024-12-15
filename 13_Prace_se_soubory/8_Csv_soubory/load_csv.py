import csv

def load_companies_with_ico():
    output = list()

    with open("company.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[3]:
                output.append(row)
    
    return output

if __name__ == "__main__":
    loaded_csv = load_companies_with_ico()

    for record in loaded_csv:
        print(record[0], record[1])
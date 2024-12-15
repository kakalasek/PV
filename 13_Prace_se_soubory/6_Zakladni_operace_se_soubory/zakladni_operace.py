import pickle
import datetime
import os

#zakladni format info
info = { 'pocet_spusteni': 0, 'posledni_spusteni': None }


if __name__ == "__main__":
    data = dict

    if not os.path.isfile("spusteni.dat"):
        with open("spusteni.dat", "wb") as file:
            pickle.dump(info, file)

    with open("spusteni.dat", "rb") as file:
        #deserializace do objektu
        data = pickle.load(file)
        print(data)

    #po kazdem spusteni provest
    data['pocet_spusteni'] += 1
    data['posledni_spusteni'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("spusteni.dat", "wb") as file:
        pickle.dump(data, file)


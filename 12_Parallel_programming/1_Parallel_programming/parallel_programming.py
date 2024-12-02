import time
import multiprocessing

def vypis_cisel():
    for i in range(0, 10):
        print(i)
        time.sleep(i)

if __name__ == "__main__":
    print("ZACATEK PROGRAMU")
    p1 = multiprocessing.Process(target=vypis_cisel)
    p1.start()
    print("KONEC PROGRAMU")
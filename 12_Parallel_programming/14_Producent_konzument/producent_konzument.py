from time import sleep
from threading import Thread
from queue import Queue

def producent(queue: Queue):
    print('Producent zacal')
    for pismeno in ["a","h","o","j","s","v","e","t","e"]:
        if queue.full() >= 3:
            sleep(0.5)
            continue
        queue.put(pismeno)
        print("Producent vlozil do fronty pismeno : {}".format(pismeno))
        sleep(0.5)

    queue.put(-1) #Vlozeni None znamena ukonceni
    print('Producent skoncil')


def konzument(queue):
    print('Konzument zacal')
    while True:
        pismeno = queue.get()
        if pismeno == -1: #Pokud je to None, znamena to ukonceni
            break
        sleep(1)
        print("Konzument nacetl : {}".format(pismeno))
    print('Konzument skoncil')


if __name__ == "__main__":
    queue = Queue(maxsize=3)

    konzument = Thread(target=konzument, args=(queue,))
    producent = Thread(target=producent, args=(queue,))

    konzument.start()
    producent.start()

    producent.join()
    konzument.join()
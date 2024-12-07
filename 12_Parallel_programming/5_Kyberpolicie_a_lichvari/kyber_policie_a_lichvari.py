import csv
import time
import hashlib
import multiprocessing
from threading import Thread


class HledejProcess(multiprocessing.Process):
    def __init__(self, od, do, hash_rc):
        super().__init__()
        self._od = od
        self._do = do
        self._hash_rc = hash_rc

    #Na nize uvedeny zdrojovy kod v uloze 12.6 nesahat !
    def hledej(self, od, do, hash_rc):
        i = 0
        with open('dluznici.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)  #preskoci prvni radek s hlavickou
            for row in reader:
                if i > od and i < do and hashlib.sha384(row[1].encode()).hexdigest() == hash_rc:
                    print("Nalezen zaznam na radku {} pro rodne cislo {} s dluhem {} CZK.".format(row[0],row[1], row[2]))
                    break
                i = i+1

    def run(self):
        self.hledej(self._od, self._do, self._hash_rc)

class HledejThread(Thread):
    def __init__(self, od, do, hash_rc):
        super().__init__()
        self._od = od
        self._do = do
        self._hash_rc = hash_rc

    #Na nize uvedeny zdrojovy kod v uloze 12.6 nesahat !
    def hledej(self, od, do, hash_rc):
        i = 0
        with open('dluznici.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)  #preskoci prvni radek s hlavickou
            for row in reader:
                if i > od and i < do and hashlib.sha384(row[1].encode()).hexdigest() == hash_rc:
                    print("Nalezen zaznam na radku {} pro rodne cislo {} s dluhem {} CZK.".format(row[0],row[1], row[2]))
                    break
                i = i+1

    def run(self):
        self.hledej(self._od, self._do, self._hash_rc)

if __name__ == "__main__":

    hash_hledaneho_rc = "5275a2bd25897f396e5f1de8b1ede4fe94d960b20619c772a3b4eccd04430afdabc44e5d388f175aa72428e009ff927c"
    start = time.time()
    """ One Process
    p1 = HledejProcess(0, 3_000_000, hash_hledaneho_rc)
    p1.start()
    p1.join()
    """
    """ Processes
    p1 = HledejProcess(0, 750_000, hash_hledaneho_rc)
    p2 = HledejProcess(750_001, 1_500_000, hash_hledaneho_rc)
    p3 = HledejProcess(1_500_001, 2_250_000, hash_hledaneho_rc)
    p4 = HledejProcess(2_250_001, 3_000_000, hash_hledaneho_rc)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    """
    """ Threads
    t1 = HledejThread(0, 1_500_000, hash_hledaneho_rc)
    t2 = HledejThread(1_500_001, 3_000_000, hash_hledaneho_rc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    """
    end = time.time()

    print("Vypocet bez trval {:.6f} sec.".format((end - start)))
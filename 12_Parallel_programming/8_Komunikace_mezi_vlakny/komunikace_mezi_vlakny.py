import csv
import time
import hashlib
import multiprocessing
from threading import Thread

zaznam = None

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
                    zaznam = [row[0], row[1], row[2]]
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
        global zaznam
        with open('dluznici.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)  #preskoci prvni radek s hlavickou
            for row in reader:
                if zaznam is not None:
                    print("breaking")
                    break
                if i > od and i < do and hashlib.sha384(row[1].encode()).hexdigest() == hash_rc:
                    zaznam = [row[0], row[1], row[2]]
                    break
                i = i+1

    def run(self):
        self.hledej(self._od, self._do, self._hash_rc)

if __name__ == "__main__":

    hash_hledaneho_rc = "5275a2bd25897f396e5f1de8b1ede4fe94d960b20619c772a3b4eccd04430afdabc44e5d388f175aa72428e009ff927c"
    start = time.time()
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
    """
    t1 = HledejThread(0, 500_000, hash_hledaneho_rc)
    t2 = HledejThread(500_001, 1_000_000, hash_hledaneho_rc)
    t3 = HledejThread(1_000_001, 1_500_000, hash_hledaneho_rc)
    t4 = HledejThread(1_500_001, 2_000_000, hash_hledaneho_rc)
    t5 = HledejThread(2_000_001, 2_500_000, hash_hledaneho_rc)
    t6 = HledejThread(2_500_001, 3_000_000, hash_hledaneho_rc)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    
    print("Nalezen zaznam na radku {} pro rodne cislo {} s dluhem {} CZK.".format(zaznam[0],zaznam[1], zaznam[2]))
    end = time.time()

    print("Vypocet bez trval {:.6f} sec.".format((end - start)))
import threading
from multiprocessing.pool import ThreadPool

class BankovniUcet:
    def __init__(self, zustatek):
        self.zustatek = zustatek
    def vloz_mince(self,pocetKusu, mince):
        for i in range(0, pocetKusu):
            self.zustatek += mince
    def __str__(self):
        return "Bankovni ucet se zustatkem: {:d} CZK".format(self.zustatek)
    

mujUcet = BankovniUcet(0)

pool = ThreadPool()

args = [(1000, 1), (1000, 2), (1000, 5), (1000, 10)]

pool.starmap(func=mujUcet.vloz_mince, iterable=args)

print(mujUcet)
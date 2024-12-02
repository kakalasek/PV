import time
import multiprocessing

class VypisCislaProcess(multiprocessing.Process):
    def __init__(self, od, do):
        super().__init__()
        self._od = od
        self._do = do

    def vypis_cisel(self, od, do):
        for i in range(od,do):
            print(i)
            time.sleep(1)

    def run(self):
        self.vypis_cisel(self._od, self._do)


if __name__ == "__main__":
    print("ZACATEK")
    p1 = VypisCislaProcess(1, 5)
    p1.start()
    p1.join()
    print("KONEC")
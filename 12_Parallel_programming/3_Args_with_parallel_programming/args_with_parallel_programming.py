import time
import multiprocessing

def vypis_cisel(od, do):
    for i in range(od,do):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=vypis_cisel, args=[1, 5])
    p1.start()
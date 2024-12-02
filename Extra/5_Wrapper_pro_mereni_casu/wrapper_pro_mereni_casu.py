import time

def tri_na_sedm_milionu():
    return 3 ** 7000000

start_time = time.time()
tri_na_sedm_milionu()
end_time = time.time()
print("Vypocet trval "+str((end_time-start_time))+"sec")

def elapsed_time(f):
    def count_elapsed_time():
        start_time = time.time()
        f()
        end_time = time.time()
        print("Vypocet trval "+str((end_time-start_time))+"sec")

    return count_elapsed_time

@elapsed_time
def tri_na_sedm_milionu():
    return 3 ** 7000000

tri_na_sedm_milionu()
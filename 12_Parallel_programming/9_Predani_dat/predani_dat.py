import threading

nakupniSeznam = ["Mleko","Maslo","Rohlik"]

def doplnNakupniSeznam(novaPolozka):
    nakupniSeznam.append(novaPolozka)
    
p1 = threading.Thread(target=doplnNakupniSeznam, args=("Chleb",))
p1.start()
p1.join()

print(nakupniSeznam)
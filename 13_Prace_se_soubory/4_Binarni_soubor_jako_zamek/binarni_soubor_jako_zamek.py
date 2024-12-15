import os
from pathlib import Path

def check_existence(filepath: str):
    file = Path(filepath)
    if not file.is_file():
        with open(filepath, "wb") as binaryFile:
            binaryFile.write(b'\x00')

def write_lock(filepath: str, data: str):
    with open(filepath, 'rb+') as lock:
        sign = lock.read(1)
        if sign == b'\x00':
            lock.seek(0)
            lock.write(b'\xFF')
        else:
            raise PermissionError
        
        lock.write(data.encode())
        lock.seek(0)
        lock.write(b'\x00')

if __name__ == "__main__":
    try:
        check_existence("lock.dat")
        write_lock("lock.dat", "Hello there")
    except PermissionError:
        print("There is already another running instance of this program")
with open('lock.dat', 'b') as file:
    lock = file.read(1)
    if lock is None:
        file.seek(0)
        file.write(b'\x00')
    
    if file.read(0) == b'\x00':
        pass
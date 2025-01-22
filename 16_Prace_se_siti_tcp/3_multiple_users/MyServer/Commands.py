import socket
from datetime import date
import random

def returnCitat():
    citaty = ["Nahodny citat 1", "Nahodny citat 2", "Nahodny citat 3"]
    return random.choice(citaty).encode('utf-8')

def returnDatum():
    today = date.today()
    return today.strftime(f'%Y-%m-%d').encode('utf-8')
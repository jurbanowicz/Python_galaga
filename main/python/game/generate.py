import random
import time
import numpy as np

from settings import *

def stage(stage_no: int) -> dict:
    n = stage_no*5 -random.randint(0,4)

    T = [3*n//255]*4

    for i in range(4):
        T[i] += n % 4
        n //= 4
    return {'fighter' : T[0], 'striker' : T[1], 'heavy' : T[2], 'destroyer' : T[3]}


def booster_type():
    booster = random.choice(list(booster_data.keys()))
    return booster

def random_interval(mu: int = 8):
    # Ustal optymalną średnią częstotliwość pojawiania się boosterów
    mean_interval = mu 
    
    # Wygeneruj losowy czas zgodnie z rozkładem wykładniczym
    interval = np.random.exponential(mean_interval)
    
    # Zwróć czas oczekiwania, zaokrąglony do 2 miejsc po przecinku
    return round(interval, 2)
    
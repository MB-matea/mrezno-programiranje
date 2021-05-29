#threading_primjer_.py
#Mrežno programiranje LABno6 2019

import _thread
import time
import datetime
from local_machine_info import print_machine_info

print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
print('Program se izvodi na ovom računalu: ')
print_machine_info()

print('--------------------------------------------------------------')

# Definicija funkcije za nit
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ('%s: %s' % ( threadName, time.ctime(time.time()) ))
# Kreiramo dvije niti
try:
    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print ("Greška: ne mogu pokrenuti nit!!")
# Čekaj dok se sve niti ne izvrše
while 1:
    pass
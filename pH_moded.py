import csv
from multitest import MultiTest
from time import time, sleep

print('Введите номер COM-порта')
cp = input()
print('')
print('Введите сетевой номер мультитеста')
nn = input()


pH_meter = MultiTest("COM{cp}", nn) 
print('')
print('Введите название файла')
name = input()

print('')
print('Введите длительность измерения в секундах')
lenght = input()

pH, t = pH_meter.get_pX()[1], 0 

startTime1 = time()  
with open(f'{name}.csv', 'w', newline='') as f: 
    w = csv.writer(f, delimiter=';')  
    w.writerows([['t, min', 'pH']]) 


while t < lenght: 
    i = time()
    with open(f'{name}.csv', 'a', newline='') as f: 
        w = csv.writer(f, delimiter=';')
        w.writerows([[t, pH]])  
    j = time()
    print(f'{t} min * {pH}') 
    t = round(time()- startTime1, 3) # t в секундах
    pH = pH_meter.get_pX()[1] 
  

    
    

import os
import time

import csv
import datetime


hosts = ["8.8.8.8","1.1.1.1", "192.168.1.1" ]

with open("ping_loh.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time","Status"])
    
while True:
    print("kättesadavuse kontroll")
    now = datetime.datetime.now()
    result = "OK"
    for elem in hosts:
        response = os.system(f"ping -n 1 {elem} > null")
        if response == 0:
            result = "OK"
            print(elem, "kättesadavalt")
        else:
            result = "Fail"
            print(elem, "ei ole kättesadavalt")
            
            
        with open("ping_loh.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now,result])
            
        print("-"*30)
        time.sleep(5)
        
        
        

import csv
import os
import requests

domain = input("Enter the domain : ")
org = input("Enter the org example: .com, .in, .pk etc... : ")
with open('demosub.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        sub = line[0]
        url = ("https://"+sub+"."+domain+org)  #https://example.com
        print(url)
        try:
            r = requests.get(url, allow_redirects=False)
            code = r.status_code
            stat = url + "   <---- [ {} ]".format(r.status_code)
            print(stat)
            f = open(domain+".csv", "a+")
            f.write(stat+ '\n')
        except:
            print("URL not found")
      

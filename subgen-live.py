import csv
import os
import requests
from colorama import init
from termcolor import colored

def banner():
    print(colored("  __        __                  ___ ",'cyan'))
    print(colored(" /__` |  | |__) __ |    | \  / |__  ",'cyan'))
    print(colored(" .__/ \__/ |__)    |___ |  \/  |___ ",'cyan'))
    print("")
    print(colored("    Author: Hariharan",'green'))
                                   
banner()
print("")
domain = input("Enter the domain : ")
print("")
org = input("Enter the org example: .com, .in, .pk etc... : ")
print("")
with open('demosub.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        sub = line[0]
        url = ("https://"+sub+"."+domain+org)  #https://example.com
        print("")
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
      

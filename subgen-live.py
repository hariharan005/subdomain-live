import csv
import os
import requests
from colorama import init
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor
import time

def banner():
    print(colored("  __        __                  ___ ", 'cyan'))
    print(colored(" /__` |  | |__) __ |    | \  / |__  ", 'cyan'))
    print(colored(" .__/ \__/ |__)    |___ |  \/  |___ ", 'cyan'))
    print("")
    print(colored("    Author: Hariharan", 'green'))

banner()
print("")
domain = input("Enter the domain : ")
print("")
org = input("Enter the org example: .com, .in, .pk etc... : ")
print("")

start_time = time.time()  # Record the start time

def process_line(line):
    sub = line[0]
    url = f"https://{sub}.{domain}{org}"  # https://example.com
    print("")
    print(url)
    try:
        r = requests.get(url, allow_redirects=False)
        code = r.status_code
        stat = f"{url}   <---- [ {code} ]"
        print(stat)
        with open(f"{domain}.txt", "a+") as f:
            f.write(stat + '\n')
    except Exception:
        print("URL not found")

# Use ThreadPoolExecutor for parallelization
with ThreadPoolExecutor(max_workers=20) as executor:  # Adjust max_workers as needed
    with open('subdomain.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        executor.map(process_line, csvreader)

end_time = time.time()  # Record the end time
process_completion_time_seconds = end_time - start_time
process_completion_time_minutes = process_completion_time_seconds / 60  # Convert seconds to minutes

print(f"\nProcess completed in {process_completion_time_minutes:.2f} minutes.")

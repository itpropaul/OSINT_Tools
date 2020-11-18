'''
TorGrab - By Shandyman
Version: 1.1
Last Update: 18/11/20
'''

import os
import sys
import csv
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

os.system('color')
class colors:
    orange = '\033[9m'
    grey = '\033[90m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    default = '\033[0m'
    
def main():
    print(f"{colors.cyan}\nWelcome to TORGrab.\n{colors.default}")
    
    try:
        query = str(sys.argv[1])
        if query == "-h":
            help()
        else:
            try:
                results = int(sys.argv[2])
                print(f"Attempting to fetch up to {colors.green}" + str(results) + f"{colors.default} results...")
            except:
                results = 10
                print(f"Attempting to fetch up to {colors.green}" + str(results) + f"{colors.default} results...")
            ahmia(query, results)
    except:
        print(f"{colors.yellow}Enter an Argument!{colors.default}")
        sys.exit()
        
def ahmia(query, results):
    
    print(f"Scanning Ahmia for: {colors.yellow}" + query + f"{colors.default}\n")
    url = "https://ahmia.fi/search/?q=" + query
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text,'html.parser')
    
    try:
        error = soup.find(id='noResults').get_text()
        error = error.strip()
    except:
        error = ""
    
    if error.startswith("Sorry"):
        print(f"{colors.yellow}Sorry, no Results!{colors.default}")
    else:
        title_results = []
        url_results = []
        lastseen_results = []
        
        print(f"{colors.cyan}============\n{colors.default}")
        
        i = 0
        for i in range(0,results):
            try:
                titles = soup.find_all('h4')[i].get_text()
                titles = titles.strip()
                title_results.append(titles)
                
                lastSeen = soup.find_all(class_='lastSeen')[i].get_text()
                lastSeen = lastSeen.strip()
                lastseen_results.append(lastSeen)
                
                urls = soup.find_all('cite')[i].get_text()
                url_results.append(urls)
                
                print(str(i+1) + f"{colors.green} [+] {colors.default}" + titles)
                print("Onion Link: " + urls)
                print("Last Active: " + lastSeen)
                print("")
                print(f"{colors.cyan}============\n{colors.default}")
            except:
                print("End of Results!")
                break
        
        ## Save the Results to CSV.
        filename = "Results - " + str(query) + ".csv"
        b = 0
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            info = csv.writer(file)
            info.writerow(["ID", "Title", "URL"])
            for a in range(0,i):
                info.writerow([b, str(title_results[b]), url_results[b]])
                b += 1
                

def help():
    
    print(f"{colors.cyan}------{colors.default}")
    print("SCRIPT SYNTAX:")
    print(f"torgrab.py {colors.green}<QUERY> <NUMBER_OF_RESULTS>{colors.default}")
    print("")
    print("EXAMPLES:")
    print("torgrab.py databases 50")
    print("torgrab.py facebook 20")
    print(f"{colors.cyan}------{colors.default}")
    
if __name__ == "__main__":
    main()

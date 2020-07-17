'''
TorGrab - By Shandyman
Version: 1.0
Last Update: 17/7/20
'''
import os
import sys
import csv
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    print("Welcome to TORGrab.")
    
    try:
        query = str(sys.argv[1])
        try:
            results = int(sys.argv[2])
        except:
            print("Returning default amount - 10.")
            results = 10
    except:
        print("Enter an Argument!")
        sys.exit()
    
    if query == "-h":
        help()
    else:
        ahmia(query, results) ## PROD FUNCTION


def ahmia(query, results):
    
    print("Scanning Ahmia for: " + query + "\n")
    ##### Create the Request #####
    url = "https://ahmia.fi/search/?q=" + query
    response = requests.get(url, verify=False)
    
    
    ##### Parse for the Data We Care About ######
    soup = BeautifulSoup(response.text,'html.parser')
    
    try:
        error = soup.find(id='noResults').get_text()
        error = error.strip()
    except:
        error = ""
    
    if error.startswith("Sorry"):
        print("Sorry, no Results!")
    else:
        title_results = []
        url_results = []
        lastseen_results = []
        
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
                
                print(str(i+1) + " [+] " + titles)
                print(urls)
                print("Last Seen: " + lastSeen)
                print("")
                print("============")
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
    
    print("\n")
    print("SCRIPT SYNTAX:")
    print("torgrab.py <QUERY> <NUMBER_OF_RESULTS>")
    print("")
    print("EXAMPLES:")
    print("torgrab.py databases 50")
    print("torgrab.py facebook 20")
    
if __name__ == "__main__":
    main()

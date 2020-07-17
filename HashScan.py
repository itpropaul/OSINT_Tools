'''
HashScan - By Shandyman
Version: 1.1
Last Update: 17/7/20
'''

import sys
import csv
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
global filebreak

filebreak = "################"
varbreak = "-----------------"
def hashes(target_hash):
    
    api_key = "<API KEY HERE>"
    
    base_url = "https://hashes.org/api.php?key="
    query_url = "&query="
    
    final_url = base_url + api_key + query_url + target_hash
    
    print(varbreak+varbreak+varbreak)
    print("\nSearching for: " + str(target_hash) + "\n")
    
    try:
        response = requests.get(final_url, verify=False)
        info = json.loads(response.content)
        
        print(info)
        try:
            plain_pass = info["result"][target_hash]["plain"]
            plain_alg = info["result"][target_hash]["algorithm"]
            
            print(filebreak)
            print("Algorithm: " + str(plain_alg))
            print("Password: " + str(plain_pass))
            print(filebreak + "\n")
        except:
            print(filebreak)
            print("Couldn't find anything about that Hash!")
            print(filebreak + "\n")
    except:
        print("Error finding that Hash!")
        print(filebreak)
        
def help():
    
    print("SYNTAX:")
    print("hashscan.py <HASH>")
    print("")
    print("EXAMPLE:")
    print("hashscan.py 5f4dcc3b5aa765d61d8327deb882cf99")
    

if __name__ == "__main__":

    print("  _   _           _     ____                  ")
    print(" | | | | __ _ ___| |__ / ___|  ___ __ _ _ __  ")
    print(" | |_| |/ _` / __| '_ \\___ \  / __/ _` | '_ \ ")
    print(" |  _  | (_| \__ \ | | |___) | (_| (_| | | | |")
    print(" |_| |_|\__,_|___/_| |_|____/ \___\__,_|_| |_|")
    print("")
    try:
        target_hash = sys.argv[1]
    except:
        print("Check that input bro....")
        sys.exit()
        
    if target_hash.endswith(".txt"):
        print("You have selected the file: " + target_hash)

        with open(str(target_hash),'r') as fileopen:
            reader = csv.reader(fileopen) 
            for row in reader:
                firststrip = str(row).lstrip("['")
                target_hash = firststrip.rstrip("']")
                hashes(str(target_hash))
    else:
        if target_hash.endswith(".csv"):
            print("You have selected the file: " + target_hash)

            with open(str(target_hash),'r') as fileopen:
                reader = csv.reader(fileopen)
                for row in reader:
                    firststrip = str(row).lstrip("['")
                    target_hash = firststrip.rstrip("']")
                    hashes(target_hash)
        else:
            if target_hash == "-h":
                help()
            else:
                hashes(target_hash)

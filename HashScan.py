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
 
    api_key = <INSERT API KEY HERE!>
    
    base_url = "https://hashes.org/api.php?key="
    query_url = "&query="
    
    final_url = base_url + api_key + query_url + target_hash
    
    print(varbreak+varbreak+varbreak)
    print("\nSearching for: " + str(target_hash) + "\n")
    
    try:
        response = requests.get(final_url, verify=False)
        info = json.loads(response.content)
        
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

if __name__ == "__main__":

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
            hashes(target_hash)

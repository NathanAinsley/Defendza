import requests
import time
import os, sys, json



#Hunter.IO setup below
hunter = requests.get("https://api.hunter.io/v2/domain-search?domain=defendza.com&api_key=5a058ef54f72edc00322758723c3057c8dcd84c8")
hunter_query = hunter.json()
list_of_emails = []

#HaveIbeenPwned setup below
headers = {'x-li-format': 'json', 'Content-Type': 'application/json','hibp-api-key':'7ff28f39d1454874aea2db72f033d800'}
class Util:
    def Key():
        dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
        Files = (dir+"/Config/config.json")
        with open(Files, encoding="utf8") as data_file:
            for row in data_file:   
                data = json.loads(row)
                try:
                    KeyName = (data['whoisusername'])
                    Key = (data['whois'])
                    listkey = (KeyName,Key)
                except KeyError:
                    print("Error loading value from json file, please delete the config.json file and run config.exe again please")
                return listkey
def search():
    for i in range(len(hunter_query)):
        hunterJson = (hunter_query['data']['emails'][i]['value'])
        list_of_emails.append(hunterJson)
        #print(hunterJson)
    print(list_of_emails)


    for x in list_of_emails:
        try:
            test = requests.get("https://haveibeenpwned.com/api/v3/breachedaccount/" + x + "", headers=headers)
            print("The company names that have breached the email - '" + x + "' are listed below:")
            # print(test.content+"\n")
            print(test.json())
            time.sleep(2)
        except:
            print("\nThere were no breaches for this email address.")

search()
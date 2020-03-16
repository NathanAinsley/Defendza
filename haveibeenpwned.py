"""
Created on Tue Mar 03 18:15:56 2020

@author: Joe Davies
@author: Nathan Ainsley 18028669
"""
import requests
import time
import os, sys, json


class Util:
    def Key():
        """Returns API Keys stored within the Config File.

        Args:
          none.
        """
        dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
        Files = (dir+"/Config/config.json")
        with open(Files, encoding="utf8") as data_file:
            for row in data_file:   
                data = json.loads(row)
                try:
                    HunterKey = (data['HunterAPI'])
                    HIBPKey = (data['haveibeenpwned'])
                    listkey = (HunterKey,HIBPKey)
                except KeyError:
                    print("Error loading value from json file, please delete the config.json file and run config.exe again please")
                return listkey
            
class Searcher:
    def Hunter(SearchTerm):
        """Returns A list of email addresses liked to the domain name passed to it.

        Args:
          Domain (Str): Domain to be seached on.
        """
        Keys = Util.Key()
        Key = Keys[0]
        hunter = requests.get("https://api.hunter.io/v2/domain-search?domain="+SearchTerm+"&api_key="+Key)
        hunter_query = hunter.json()
        list_of_emails = []
        for i in range(len(hunter_query)):
            hunterJson = (hunter_query['data']['emails'][i]['value'])
            list_of_emails.append(hunterJson)
            #print(hunterJson)
        return list_of_emails 
    def HaveIBeenPwned(emails):
        """Returns A list of breaches if there are any for the array of emails passed to it.

        Args:
          Emails (Str): Array of domains stored as strings to be checked if there any breaches.
        """
        Keys = Util.Key()
        Key = Keys[1]
        headers = {'x-li-format': 'json', 'Content-Type': 'application/json','hibp-api-key':Key}
        breaches = []
        for x in emails:
            request = requests.get("https://haveibeenpwned.com/api/v3/breachedaccount/" + x + "", headers=headers)
            EmailBreach = []
            try:
                responce = request.json()
                EmailBreach.append(x)
                for records in responce:
                    EmailBreach.append(records)
                breaches.append(EmailBreach)
                time.sleep(2)
            except:
                EmailBreach.append(x)
                EmailBreach.append("There were no breaches for this email address")
                breaches.append(EmailBreach)
        return breaches
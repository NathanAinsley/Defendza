import whois
import socket
from urllib.request import urlopen, pathname2url
import json
import os
import sys
import requests
from urllib.request import urlopen
import http.client as http

dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
Files = (dir+"/Config/config.json")
with open(Files, encoding="utf8") as data_file:
    for row in data_file:   
        data = json.loads(row)
        try:
            KeyName = (data['whoisusername'])
            Key = (data['whois'])
            Key = 'at_PrAK3diGVNKNEndontcjJgs8C2wFD'
            print(KeyName,Key)
        except KeyError:
            print("Error loading value from json file, please delete the config.json file and run config.exe again please")

class Setup:
    def Domains(v):
        com = v + ".com"
        couk = v + ".co.uk"
        uk = v + ".uk"
        org = v + ".org"
        net = v + ".net"
        us = v + ".us"
        de = v + ".de"
        cn = v + ".cn"
        info = v + ".info"
        nl = v + ".nl"
        eu = v + ".eu"
        ru = v + ".ru"
        Domains = [com,couk,uk,org,net,us,de,cn,info,nl,eu,ru]
        return Domains

class Searcher:
    def GetDomainInfoByName(v):
        Domains = Setup.Domains(v)
        i = 0
        Records = []
        while i < len(Domains):
            try:
                q = whois.query(Domains[i])
                Servers = q.name_servers
                Name = q.name
                CreationDate = q.creation_date
                ExpireDate = q.expiration_date
                Update = q.last_updated
                Registrar = q.registrar
                Ip = Searcher.SingleSocket(Domains[i])
                record = [((Name),(CreationDate),(ExpireDate),(Update),(Registrar),(Servers),(Ip))]
                Records.append(record)
                i+=1
            except:
                print("No Domain at: "+Domains[i])
                i+=1
        return Records
    
    

            
    def Reverse(SearchTerm1,SearchTerm2,ExcludeTerm1,ExcludeTerm2):
        

#        dolladolla = 'https://user.whoisxmlapi.com/service/account-balance?apiKey=' + password
#        ballance = requests.get(dolladolla)
#        print(response)
        
        payload_basic = {
    'basicSearchTerms': {
        'include': [
            SearchTerm1,
            SearchTerm2
        ],
        'exclude': [
            ExcludeTerm1,ExcludeTerm2
        ],
    },
    'searchType': 'current',
    'mode': 'purchase',
    'apiKey': Key,
    'responseFormat': 'json'
}
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }   
    
        conn = http.HTTPSConnection('reverse-whois-api.whoisxmlapi.com')
        
        conn.request('POST', '/api/v2', json.dumps(payload_basic), headers)

        response = conn.getresponse()
        text = response.read().decode('utf8')
        response_dict = json.loads(text)
        response_list = (response_dict['domainsList'])
        for records in response_list:
            domain = str(records)
            Searcher.GetDomainInfoByNameWithExtension(domain)
            
        
    def GetDomainInfoByNameWithExtension(Domains):
        record = ''
        try:
            q = whois.query(Domains)
            Servers = q.name_servers
            Name = q.name
            CreationDate = q.creation_date
            ExpireDate = q.expiration_date
            Update = q.last_updated
            Registrar = q.registrar
            Ip = Searcher.SingleSocket(Domains)
            record = [((Name),(CreationDate),(ExpireDate),(Update),(Registrar),(Servers),(Ip))]
            Searcher.SinglePrint(record)
        except:
            print("No Domain at: "+Domains)


        
    def SingleSocket(v):
        d = socket.gethostbyname(v)
        return d
    
    def SinglePrint(records):
        for record in records:
            try:
                print("Domain Name: " + str(record[0]))
            except:
                print("No Domain Name Listed")
            try:
                print("Creation Date: " + str(record[1]))
            except:
                print("No Domain Name Listed")
            try:
                print("Expiration Date: " + str(record[2]))
            except:
                print("No Expiration Date Listed")
            try:
                print("Last Updated: " + str(record[3]))
            except:
                print("No Expiration Date Listed")
            try:
                print("Registrar name: " + str(record[4]))
            except:
                print("No Registrar Name listed")
            try:
                print("Servers: " + str(record[5]))
            except:
                print("No Servers Listed")
            try:
                print("IP Address: " + str(record[6]))
            except:
                print("No IP Address linked")
            print("\n \n \n")
        
    def printer(returned):
        for records in returned:
            for record in records:
                try:
                    if Searcher.SingleSocket(record[0]) != None: 
                        try:
                            print("Domain Name: " + str(record[0]))
                        except:
                            print("No Domain Name Listed")
                        try:
                            print("Creation Date: " + str(record[1]))
                        except:
                            print("No Domain Name Listed")
                        try:
                            print("Expiration Date: " + str(record[2]))
                        except:
                            print("No Expiration Date Listed")
                        try:
                            print("Last Updated: " + str(record[3]))
                        except:
                            print("No Expiration Date Listed")
                        try:
                            print("Registrar name: " + str(record[4]))
                        except:
                            print("No Registrar Name listed")
                        try:
                            print("Servers: " + str(record[5]))
                        except:
                            print("No Servers Listed")
                        try:
                            print("IP Address: " + str(record[6]))
                        except:
                            print("No IP Address linked")
                        print("\n \n \n")
                except:
                    pass
                    
        
#returned = Searcher.GetDomainInfoByName('Defendza')
#Searcher.printer(returned)
Searcher.Reverse('SpaceX','US','Europe','EU')
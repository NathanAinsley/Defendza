from urllib.request import urlopen, pathname2url
import json
import os
import sys
import http.client as http
from urllib.request import urlopen
from pprint import pprint
import socket



class Util:
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
    def DeleteContents(file):
        with open(file,"w"):
            pass
    def printer(returned):
        pprint(returned)
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

class WhoIs:

    
    def GetDomainInfoByName(domainName):
        Key = Util.Key()
        KEY = Key[1]
        url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName=' + domainName + '&apiKey=' + KEY + "&outputFormat=JSON"
        Data = (urlopen(url).read().decode('utf8'))
        r = json.loads(Data)
        r = r['WhoisRecord']
        
        return(r)
        
        
    def Reverse(SearchTerm1,SearchTerm2,ExcludeTerm1,ExcludeTerm2):
        
        Key = Util.Key()
        KEY = Key[1]
        
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
                        'apiKey': KEY,
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
        Util.DeleteContents("reverseWhoIsOutput.json")
        for records in response_list:
            domain = str(records)
            Data=(WhoIs.GetDomainInfoByName(domain))
            with open("reverseWhoIsOutput.json",'a',encoding='utf-8') as outfile1:
                json.dump(Data,outfile1,ensure_ascii=False,indent=4)

    def GetIP(domainName):
        IP = socket.gethostbyname(domainName)
        return IP
        
class DNS:
    def DNS_Lookup(domain):
        Key = Util.Key()
        KEY = Key[1]
        Type = '_all'
        Format = 'JSON'
        
        url = 'https://www.whoisxmlapi.com/whoisserver/DNSService?'+ 'apiKey=' + KEY + '&domainName=' + domain + '&type=' + Type +'&outputFormat=' + Format
        data = (urlopen(url).read().decode('utf8'))
        r=json.loads(data)
        return r
    
    
        
    
Util.printer(WhoIs.GetDomainInfoByName('defendza.com'))              
#DNS.DNS_Lookup('defendza.com')
#WhoIs.Reverse('SpaceX','US','Europe','EU')
#print(WhoIs.GetIP('Defendza.com'))
from shodan import Shodan
import json
import os
import sys
#https://github.com/achillean/shodan-python
dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
Files = (dir+"/Config/config.json")
with open(Files, encoding="utf8") as data_file:
    for row in data_file:   
        data = json.loads(row)
        try:
            Key = (data['Shodan'])
            print(Key)
        except KeyError:
            print("Error loading value from json file, please delete the config.json file and run config.exe again please")

api = Shodan(Key)

class Shodan:
    def Shodan(v):
        ipinfo = api.host(v)
        try:
            regional_code = ipinfo['region_code']
        except:
            regional_code = 'No regional Code Recieved'
        try:
            country_code = ipinfo['country_code']
        except:
            country_code = 'No country Code Recieved'
        try:
            city = ipinfo['city']
        except:
            city = 'No City Revcieved'
        
        Returned = (regional_code,country_code,city)
        return Returned
            
        
        
print(Shodan.Shodan('184.168.221.38'))
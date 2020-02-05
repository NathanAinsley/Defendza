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
        return (ipinfo)
from shodan import Shodan
import json
import os
import sys


class ShodanSearcher:
    def KEY():
        dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
        Files = (dir+"/Config/config.json")
        with open(Files, encoding="utf8") as data_file:
            for row in data_file:   
                data = json.loads(row)
                try:
                    Key = (data['Shodan'])
                except KeyError:
                    print("Error loading value from json file, please delete the config.json file and run config.exe again please")
        
        
        return(Key)
    def Shodan(v):
        Key = ShodanSearcher.KEY()
        api = Shodan(Key)
        ipinfo = api.host(v)
        cves = []
        try:
            regional_code = ipinfo['region_code']
        except:
            regional_code = 'No regional Code Recieved'
        try:
            country_code = ipinfo['country_code']
        except:
            country_code = 'No country Code Recieved'
        try:
            country_name = ipinfo['country_name']
        except:
            country_name = 'No country name Recieved'
        try:
            city = ipinfo['city']
        except:
            city = 'No City Revcieved'
        try:
            postal_code = ipinfo['postal_code']
        except:
            postal_code = 'No Postal code listed'
        try:
            dma_code = ipinfo['dma_code']
        except:
            dma_code = 'No Dma Code Recieved'
        try:
            last_update = ipinfo['last_update']
        except:
            last_update = 'No Date given for last Update'
        try:
            tags = ipinfo['tags']
        except:
            tags = 'No Tags Listed'
        try:
            lat = ipinfo['latitude']
            lon = ipinfo['longitude']
            coords = (str(lat) + ',' + str(lon))
        except:
            coords = 'No Coords Listed'
        try:
            org = ipinfo['org']
        except:
            org = 'No org listed'
        try:
            ports = ipinfo['ports']
        except:
            ports = 'No ports listed'
            
        
        Data = ipinfo['data']
        for records in Data:
            try:
                data = (records['vulns']).items()
                for record in data:
                    CVES = []
                    cve = record[0]
                    CVES.append(cve)
                    
                    DATA = record[1]
                    
                    references = DATA['references']
                    CVES.append(references)
                    
                    verified = DATA['verified']
                    CVES.append(verified)
                    
                    cvss = DATA['cvss']
                    CVES.append(cvss)
                    
                    cves.append(CVES)
            except:
                pass
                
                
            
                
            
        
        Returned = (regional_code,country_code,country_name,city,postal_code,dma_code,last_update,tags,coords,org,ports,cves)
        return Returned
    def printer(v):
        try:
            print('regional code: ' + v[0])
        except:
            print("Error with Regional Code")
        try:
            print('country code: ' + v[1])
        except:
            print("Error with Country Code")
        try:
            print('country name: ' + v[2])
        except:
            print("Error with Country Name")
        try:
            print("city: " + v[3])
        except:
            print("Error with City")
        try:
            print('postal code: ' + v[4])
        except:
            print("Error with Postal Code")
        try:
            print('dma code: ' + v[5])
        except:
            print("Error with DMA Code")
        try:
            print('last_update: ' + str(v[6]))
        except:
            print("Error with Last Update")
        try:
            print('tags: ' + v[7])
        except:
            print("Error with Tags")
        try:
            print('coordinates: ' + str(v[8]))
        except:
            print("Error with Coordinates")
        try:
            print('organisation: ' + v[9])
        except:
            print("Error with Organisation")
        try:
            print('ports: ' + str(v[10]))
        except:
            print("Error with Ports")
        try:
            print('cves: ' + str(v[11]))
        except:
            print("Error with CVEs")
            
ShodanSearcher.printer(ShodanSearcher.Shodan("104.198.14.52"))
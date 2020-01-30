import os
import sys
import json
import glob
import chwrapper
_BASE_URL = "https://api.companieshouse.gov.uk/"
dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
Files = (dir+"/Config/config.json")
with open(Files, encoding="utf8") as data_file:
    for row in data_file:   
        data = json.loads(row)
        try:
            Key = (data['companieshouse'])
        except KeyError:
            print("Error loading value from json file, please delete the config.json file and run config.exe again please")
print (Key)


class Searcher():
    def CompanyNumberFromName(Name):
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.search_companies(Name)
        r = r.json()
        Company_Number = (r['items'][0]['company_number'])
        print (Company_Number)
        return Company_Number
    def CompanyAddressFromNumber(Number):
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.address(Number)
        r = r.json()
        AddressLine1 = r['address_line_1']
        AddressLine2 = r['address_line_2']
        Country = r['country']
        Locality = r['locality']
        Postcode = r['postal_code']
        Address = AddressLine1 +','+AddressLine2+','+Country+','+Locality+','+Postcode
        print(Address)
        return Address
    def CompanyStakeHoldersByNumber(Number):
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.persons_significant_control(Number)
        r = r.json()
        print(r)
        #will return a list of all stake holders in the company, including their personal details.
    def CompanyProfileByNumber(Number):
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.profile(Number)
        r = r.json()
        print(r)
        #returns the company profile
        
CompanyNum = Searcher.CompanyNumberFromName('Defendza')
Searcher.CompanyAddressFromNumber(CompanyNum)
Searcher.CompanyProfileByNumber(CompanyNum)
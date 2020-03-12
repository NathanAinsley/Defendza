import os
import sys
import json
import chwrapper
_BASE_URL = "https://api.companieshouse.gov.uk/"



class Searcher():
    def Key():
        """Returns API Key stored within the Config File.

        Args:
          none.
        """
        dir = (os.path.dirname(os.path.realpath(sys.argv[0])))
        Files = (dir+"/Config/config.json")
        with open(Files, encoding="utf8") as data_file:
            for row in data_file:   
                data = json.loads(row)
                try:
                    Key = (data['companieshouse'])
                except KeyError:
                    print("Error loading value from json file, please delete the config.json file and run config.exe again please")
            return Key
    def getCompanyNumberFromName(Name):
        """Returns string containing the company number.

        Args:
          Number (str): Company name to search on.
        """
        Key = Searcher.Key()
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.search_companies(Name)
        r = r.json()
        Company_Number = (r['items'][0]['company_number'])
        return Company_Number
    def getCompanyAddressFromNumber(Number):
        """Returns string containing the company address.

        Args:
          Number (str): Company number to search on.
        """
        Key = Searcher.Key()
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.address(Number)
        r = r.json()
        try:
            AddressLine1 = r['address_line_1']
        except:
            AddressLine1 = "AddressLine1 Value Missing"
        try:
            AddressLine2 = r['address_line_2']
        except:
            AddressLine2 = "AddressLine2 Value Missing"
        try:
            Country = r['country']
        except:
            Country = "Country Value Missing"
        try:
            Locality = r['locality']
        except:
            Locality = "Localiy Value Missing"
        try:
            Postcode = r['postal_code']
        except:
            Postcode = "Postcode Value Missing"
        Address = AddressLine1 +','+AddressLine2+','+Country+','+Locality+','+Postcode
        return Address
    def getCompanyStakeHoldersByNumber(Number):
        """Returns a list of all steakholders within the company.

        Args:
          Number (str): Company number to search on.
        """
        Key = Searcher.Key()
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.persons_significant_control(Number)
        r = r.json()
        Members=[]
        i = 0
        for row in r['items']:
            try:
                Name = r['items'][i]['name']
            except:
                Name = "Name Value Missing"
            try:
                month = r['items'][i]['date_of_birth']['month']
            except:
                month = "Month Value Missing"
            try:
                year = r['items'][i]['date_of_birth']['year']
            except:
                year = "Year Value Missing"
            DOB = str(month)+"/"+str(year)
            member=str(Name)+","+str(DOB)
            Members.append(member)
            i+=1
        return Members
    def getFillingHistory(Number):
        """Returns a list of all files that have been filed by the company.

        Args:
          Number (str): Company number to search on.
        """
        Key = Searcher.Key()
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.filing_history(Number)
        r = r.json()
        Files = []
        i = 0
        for row in r['items']:
            try:
                Date = r['items'][i]['date']
            except:
                Date = "No Date Found"
            try:
                Category = r['items'][i]['category']
            except:
                Category = "No Category Found"
            try:
                Description = r['items'][i]['description']
            except:
                Description = "No Description Found"
            try:
                Type = r['items'][i]['type']
            except:
                Type = "No Type Found"
            try:
                Page = r['items'][i]['pages']
            except:
                Page = "No Pages Found"
            try:
                Barcode = r['items'][i]['barcode']
            except:
                Barcode = "No Barcode Found"
            Doc = ("Date: " + str(Date) + "," +
                   "Category: " + str(Category) + "," +
                   "Description: " + str(Description) + "," +
                   "Type: " + str(Type) + "," +
                   "Page: " + str(Page) + "," +
                   "Barcode: " + str(Barcode) )
            i+=1
            Files.append(Doc)
        return Files
    
    def getFilingAmount(Number):
        """Returns the amount of files filed by the company.

        Args:
          Number (str): Company number to search on.
        """
        Key = Searcher.Key()
        search_client=chwrapper.Search(access_token=Key)
        r = search_client.filing_history(Number)
        r = r.json()
        try:
            FilingAmount = r['total_count']
        except:
            FilingAmount = "No FilingAmount Found"
        return FilingAmount


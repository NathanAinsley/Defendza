import json

checker = "n"
finalcheck = "n"
while finalcheck != "y":
    while checker !="y":
        CompaniesHouseAPI=str(input("Please enter the Companies House Api Key: "))
        print("Is " + CompaniesHouseAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        WhoIsXMLUserName=str(input("Please enter the WhoIsXML Api Username: "))
        print("Is " + WhoIsXMLUserName + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        WhoIsXML=str(input("Please enter the WhoIsXML Api Key: "))
        print("Is " + WhoIsXML + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        ShodanAPI=str(input("Please enter the Shodan Api Key: "))
        print("Is " + ShodanAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        HunterAPI=str(input("Please enter the Hunter Api Key: "))
        print("Is " + HunterAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        PwnedAPI=str(input("Please enter the HaveIBeenPwned Api Key: "))
        print("Is " + PwnedAPI + " correct?")
        checker = str(input("(y/n)"))
    finalcheck = str(input("Please confirm that all data entered is correct and has no mistakes, if so press (y) otherwise press (n) to start over. "))


data = {  'companieshouse':CompaniesHouseAPI ,
        'WhoIsXMLUserName':WhoIsXMLUserName ,
        'WhoIsXML':WhoIsXML ,
        'Shodan':ShodanAPI ,
        'HunterAPI':HunterAPI ,
        'haveibeenpwned':PwnedAPI}
with open('config.json','a+') as outfile:
    json.dump(data, outfile)
    
input("Values saved, please press [ENTER] to exit program now, Thank you")
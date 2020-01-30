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
        WhoIsAPI=str(input("Please enter the Whois Api Key: "))
        print("Is " + WhoIsAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        ShodanAPI=str(input("Please enter the Shodan Api Key: "))
        print("Is " + ShodanAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        LinkedinAPI=str(input("Please enter the Linkedin Api Key: "))
        print("Is " + LinkedinAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        DNSMXAPI=str(input("Please enter the DNSMX Api Key: "))
        print("Is " + DNSMXAPI + " correct?")
        checker = str(input("(y/n)"))
    checker = "n"
    while checker !="y":
        PwnedAPI=str(input("Please enter the HaveIBeenPwned Api Key: "))
        print("Is " + PwnedAPI + " correct?")
        checker = str(input("(y/n)"))
    finalcheck = str(input("Please confirm that all data entered is correct and has no mistakes, if so press (y) otherwise press (n) to start over. "))


data = {  'companieshouse':CompaniesHouseAPI ,
        'whois':WhoIsAPI ,
        'shodan':ShodanAPI ,
        'linkedin':LinkedinAPI ,
        'DNSXM':DNSMXAPI ,
        'haveibeenpwned':PwnedAPI}
with open('config.json','a+') as outfile:
    json.dump(data, outfile)
    
input("Values saved, please press [ENTER] to exit program now, Thank you")
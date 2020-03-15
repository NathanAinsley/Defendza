# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:48:23 2020

@author: Nathan
"""
from os.path import join
#from prettytable import PrettyTable
from CompanyHouse import Searcher
from haveibeenpwned import Searcher as SearcherPWN
from WhoIs import WhoIs
from WhoIs import DNS
from Shodan import ShodanSearcher
import os
import simplejson
import json

with open ("OutputOSINT.txt", 'w+', encoding="utf8" ) as outfile:
        outfile.write("")

def WhoIsMenu():
    print("+============================================+")
    print("|                  W H O - I S               |")
    print("+============================================+")
    print("|          Enter the domain of a company     |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    name = input()
    #name = str("'"+name+"'")
    returned = WhoIs.GetDomainInfoByName(name)
    
    with open ("WhoIsOutput.json", 'w') as outfile:
        json.dump(returned,outfile)
        
    osCommandString = "notepad.exe WhoIsOutput.json"
    os.system(osCommandString)
    WhoIsMainMenu()
    
    
def ReverseWhoIsMenu():
    print("+============================================+")
    print("|        R E V E R S E - W H O - I S         |")
    print("+============================================+")
    print("|          Enter the details of a company    |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    term1 = input("Enter Search term 1: ")
    term2 = input("Enter Search term 2: ")
    term3 = input("Enter Exclude term 1: ")
    term4 = input("Enter Exclude term 2: ")
    
    WhoIs.Reverse(term1,term2,term3,term4)
    
    osCommandString = "notepad.exe reverseWhoIsOutput.json"
    os.system(osCommandString)
    WhoIsMainMenu()
    
def IP():
    print("+============================================+")
    print("|                      I P                   |")
    print("+============================================+")
    print("|          Enter the domain of a company     |")
    print("|          This company will then be         |")
    print("|          searched and be outputted.        |")
    print("+============================================+")
    ip = input("Enter Domain to search IP:")
    print("IP = " + WhoIs.GetIP(ip))
    WhoIsMainMenu()
    
def DNs():
    print("+============================================+")
    print("|                     D N S                  |")
    print("+============================================+")
    print("|          Enter the domain of a company     |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    domain = input()
    returned = DNS.DNS_Lookup(domain)
    
    with open ("DNSOutput.json", 'w') as outfile:
        json.dump(returned,outfile)
    osCommandString = "notepad.exe DNSOutput.json"
    os.system(osCommandString)
    WhoIsMainMenu()
    
def WhoIsMainMenu():
    print("+============================================+")
    print("|       W H O - I S - M A I N - M E N U      |")
    print("+============================================+")
    print("|          Enter your choice [1-3]           |")
    print("|                                            |")
    print("|          1. WhoIs from domain name         |")
    print("|          2. Reverse WhoIs Search           |")
    print("|          3. IP  Search                     |")
    print("|          4. DNS Search                     |")
    print("|          5. Return to main menu            |")
    print("|                                            |")
    print("+============================================+")
    choice = input()
    choice = int(choice)
    
    if choice == 1:
        WhoIsMenu()
    if choice == 2:
        ReverseWhoIsMenu()
    if choice == 3:
        IP()
    if choice == 4:
        DNs()
    if choice == 5:
        mainmenu()
    if choice != (1,2,3,4,5):
        print("Error, please enter a valid number")
        
    

def CompaniesHouseMenu():
    print("+============================================+")
    print("|        C O M P A N I E S - H O U S E       |")
    print("+============================================+")
    print("|          Enter the name of a company       |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    name = input()
    number = Searcher.getCompanyNumberFromName(name)
    address = Searcher.getCompanyAddressFromNumber(number)
    SteakHolders = Searcher.getCompanyStakeHoldersByNumber(number)
    filling = Searcher.getFilingAmount(number)
    fillingamount = str(filling)
    
    with open ("OutputOSINT.txt", 'a', encoding="utf8" ) as outfile:
        outfile.write("+====================================================================================================+\n")
        outfile.write("|                                       COMPANIES HOUSE DATA                                         |\n")
        outfile.write("+----------------------------------------------------------------------------------------------------+\n")
        outfile.write("|                                                                                                    |\n")
        outfile.write("|   Company Name: "+name+(83-len(name))*' '+"|\n")
        outfile.write("|   Company Number: "+number+(81-len(number))*' '+"|\n")
        outfile.write("|   Company Address: "+address+(80-len(address))*' '+"|\n")
        for holders in SteakHolders:
            outfile.write("|   Steak Holder: "+holders+(83-len(holders))*' '+"|\n")
        outfile.write("|   Company Filling Amount: "+fillingamount+(73-len(fillingamount))*' '+"|\n")
        outfile.write("|                                                                                                    |\n")
        outfile.write("+====================================================================================================+\n")
        outfile.write("\n")
    
    mainmenu()
    
def HIBP():
    print("+============================================+")
    print("|      H A V E -  I - B E E N - P W N E D    |")
    print("+============================================+")
    print("|          Enter the domain of a company     |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    name = input()
    emails = SearcherPWN.Hunter(name)
    pwnedEmails = SearcherPWN.HaveIBeenPwned(emails)
    with open ("OutputOSINT.txt", 'a', encoding="utf8" ) as outfile:
        outfile.write("+====================================================================================================+\n")
        outfile.write("|                                       HAVE I BEEN PWNED?                                           |\n")
        outfile.write("+----------------------------------------------------------------------------------------------------+\n")
        outfile.write("|                                                                                                    |\n")
        for email in pwnedEmails:
            outfile.write("|   Email Address: "+email[0]+(82-len(email[0]))*' '+"|\n")
            outfile.write("|   Breaches: "+email[1]+(87-len(email[1]))*' '+"|\n")
            outfile.write("|                                                                                                    |\n")
        outfile.write("|                                                                                                    |\n")
        outfile.write("+====================================================================================================+\n")
    mainmenu()
    
def Shodan():
    print("+============================================+")
    print("|                  S H O D A N               |")
    print("+============================================+")
    print("|          Enter the IP  of a company        |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    domain = input()
    
    returned = ShodanSearcher.Shodan(domain)
    with open ("ShodanOutput.json", 'w') as outfile:
        json.dump(returned,outfile)
    osCommandString = "notepad.exe ShodanOutput.json"
    os.system(osCommandString)
    mainmenu()
    
def mainmenu():
    print("+============================================+")
    print("|        O S I N T - M A I N - M E N U       |")
    print("+============================================+")
    print("|          Enter your choice [1-5]           |")
    print("|                                            |")
    print("|                                            |")
    print("|                                            |")
    print("|          1. Companies House Search         |")
    print("|          2. Have I been Pwned              |")
    print("|          3. Who Is                         |")
    print("|          4. Shodan                         |")
    print("|          5. Open Data                      |")
    print("|                                            |")
    print("|                                            |")
    print("+============================================+")
    
    choice = input()
    choice = int(choice)
    
    if choice == 1:
        CompaniesHouseMenu()
    if choice == 2:
        HIBP()
    if choice == 3:
        WhoIsMainMenu()
    if choice == 4:
        Shodan()
    if choice == 5:
        osCommandString = "notepad.exe OutputOSINT.txt"
        os.system(osCommandString)    
        mainmenu()
    else:
        print("Error, please enter a valid number")
        mainmenu()
    
mainmenu()
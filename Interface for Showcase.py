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
    returned = WhoIs.GetDomainInfoByName(name)
    
    with open ("OutputOSINT.txt", 'a', encoding="utf8" ) as outfile:
    
    
def ReverseWhoIsMenu():
    return 0

def WhoIsMainMenu():
    print("+============================================+")
    print("|       W H O - I S - M A I N - M E N U      |")
    print("+============================================+")
    print("|          Enter your choice [1-3]           |")
    print("|                                            |")
    print("|          1. WhoIs from domain name         |")
    print("|          2. Reverse WhoIs Search           |")
    print("|          3. Return to main menu            |")
    print("|                                            |")
    print("+============================================+")
    choice = input()
    choice = int(choice)
    
    if choice == 1:
        WhoIsMenu()
    if choice == 2:
        ReverseWhoIsMenu()
    if choice == 3:
        mainmenu()
    else:
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
    print("+============================================+")
    
    choice = input()
    choice = int(choice)
    
    if choice == 1:
        CompaniesHouseMenu()
    if choice == 2:
        HIBP()
    if choice == 3:
        WhoIsMainMenu()        
    else:
        print("Error, please enter a valid number")
        mainmenu()
    
mainmenu()
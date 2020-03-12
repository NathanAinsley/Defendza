# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:48:23 2020

@author: Nathan
"""
from os.path import join
from prettytable import PrettyTable
from CompanyHouse import Searcher
# Import the necessary packages
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
    
    with open ("OutputOSINT.txt", 'w+', encoding="utf8" ) as outfile:
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
        
    mainmenu()
    
def HIBP():
    print("+============================================+")
    print("|      H A V E -  I - B E E N - P W N E D    |")
    print("+============================================+")
    print("|          Enter the name of a company       |")
    print("|          This company will then be         |")
    print("|          searched and results added        |")
    print("|          to the output file.               |")
    print("+============================================+")
    
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
    print("+============================================+")
    
    choice = input()
    choice = int(choice)
    
    if choice == 1:
        CompaniesHouseMenu()
    if choice == 2:
        HIBP()
    
mainmenu()
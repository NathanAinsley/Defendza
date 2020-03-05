# ProfDev - OSINT Program

## Modules
### Companies House
#### Use this module to get information on a company from the internet.  
To start off you will need to get the company number from the Module, todo this you will need to pass it the name of the company,
```python
CompanyHouse.Searcher.getCompanyNumberFromName(CompanyNameHere) # returns the company number
```
Once you have the Company Number you can then pass it back to the Module to gain more information out of the system.  
```python
CompanyHouse.Searcher.getCompanyAddressFromNumber(CompanyNum) # returns an address of the company if one excists
```
Running the method above will return a string containing the address of the company, if you wish to seperate the values into their components then they are seperated by single a ,  
The Values returned are:  
 - Address Line 1  
 - Address Line 2  
 - Country  
 - Locality (aka county)  
 - Postal Code  
  
  
You can also then run the following command to get details on the Company Steakholders  
```python
CompanyHouse.Searcher.getCompanyStakeHoldersByNumber(CompanyNum) # returns details on steakholders  
```
This command will return with details on the Steakholders which includes their name and date of birth. This info is returned in a list, with the name and Date of birth being again seperated by a single ,  
Values Returned are:  
 - Name  
 - Date of birth in format (mm/yyyy)  
  
  
You can also use the following command to gain all the filling that the company has done. 
```python
CompanyHouse.Searcher.getFillingHistory(CompanyNum) # returns array containing Filling details
```
Passing this function the Company number will return a rather large array on all the files that the company has filled.  
Values Returned:  
 - Date of Filling  
 - Category of Filling  
 - Description of File  
 - Type of File  
 - The Amount of Pages in File  
 - Barcode of File  
  
These values are seperated by a string and then stored as one large string within an array.  
  
  
The Final Function included is to return the amount of filling that the company has done.  
```python
CompanyHouse.Searcher.getFilingAmount(CompanyNum) # returns an int containing the amount of files the company has filled  
```
  
  
### WhoIs  
  
#### This Class and Module allows you to feed it the name of a company and return information on any website that might be linked to such a company.  
  
The main funcion of this method is the 
```python
Searcher.GetDomainInfoByName(v):
```
This Function when passed a string containing the name of the domain you want to search EXCLUDING THE EXTENSION, will then run a search against the top 10 domain extensions for any domain registered under that name.  
The function runs another function called 
```python
Setup.Domains(v)
```
which attaches to the end of the search term the top 10 domain extensions along with 2 other common ones and then returns a list containing those domain names.  
```python
def Domains(v):
        com = v + ".com"
        couk = v + ".co.uk"
        uk = v + ".uk"
        org = v + ".org"
        net = v + ".net"
        us = v + ".us"
        de = v + ".de"
        cn = v + ".cn"
        info = v + ".info"
        nl = v + ".nl"
        eu = v + ".eu"
        ru = v + ".ru"
        Domains = [com,couk,uk,org,net,us,de,cn,info,nl,eu,ru]
        return Domains
```
This Array is then Parsed and information is retrieved from the module to be returned to the user.  
  
Variables Returned:
 - Name of Domain  
 - Creation Date  
 - Expiration date  
 - Last Updated Date  
 - Registrar Details if Availible  
 - Servers Associated To Domain  
  
Some of the infomation returned might be redacted due to privacy of the owner.  
All the data returned will be seperated by a single comma in the order above, within a list.  
  
Another Method is then run along side this which is the Socket method



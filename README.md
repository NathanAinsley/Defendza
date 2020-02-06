# Defendza OSINT Program

## Modules
### Companies House
Use this module to get information on a company from the internet.  
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
Address Line 1  
Address Line 2  
Country  
Locality (aka county)  
Postal Code  

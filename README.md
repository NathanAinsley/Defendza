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

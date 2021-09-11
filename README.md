# NYPD

General Information
•	This is full list of offence of NYPC in the year of 2016 and user has an options to view two set of quires 
•	What problem does it (intend to) solve?
1.	Displaying dictionary count records group by offence description in descending order. 
2.	User has to given any (with in the specified) offence description from the list and all those records specified will be exported to CSV file. (Example : User might want to see the offence list of cases for BURGLARY/ RAPE/ FORGERY / other. 
Technologies Used
•	Used Python 3.9.7
•	Visual Studio code IDE - Version: 1.60.0 (user setup)
o	Commit: e7d7e9a9348e6a8cc8c03f877d39cb72e5dfb1ff
o	Date: 2021-09-01T10:41:52.311Z
o	Electron: 13.1.8
o	Chrome: 91.0.4472.164
o	Node.js: 14.16.0

NYPD Arrest Data 2018 – Query’s  
This project is to show few quick view of the NYPD arrest data of the year 2016 queries like 
1.	Displaying dictionary count records group by offence description in descending order. 
2.	User has to given any (with in the specified) offence description from the list and all those records specified will be exported to CSV file. (Example : User might want to see the offence list of cases for BURGLARY/ RAPE/ FORGERY / other. 

Usage
Used Python 3.9.7 and avoid using Pandas. 

Project Status
Project is:  Completed using Python 3.9.7

Room for Improvement
In case this program needs to be scaled up with huge data files we can use AWS glue. 

Second possible approach for the problem statement: 
Using Glue and Spark method we can accomplish this and more details as below: 
-	By using phyton and pyspark code. 

Q1. What file sizes does the program can handle?
-	It depends on the system configuration &with the current file size and configuration at hand this been working. 
-	However, if we need to scale for large data files we need to use glue/spark consol. 
o	It will distubuted   the file and do the needful. 
o	Glue and spark is scope of scalable options ahead. 
o	Using distubuted program we can solve the case   

Q2. What is the configuration of the system where this was run.
-	System type – x64-based PC
-	Processor	Intel(R) Core(TM) i7-3667U CPU @ 2.00GHz, 2001 Mhz, 2 Core(s), 4 Logical Processor(s)
-	BaseBoard Version	Win8 Pro DPK TPG
-	Installed Physical Memory (RAM)	8.00 GB
-	Available Virtual Memory	11.2 GB 

Acknowledgements
Enjoyed my time in coding and building a quick solution. Thank you for the opportunity. 

Special Gotchas of my project (Problems I faced, unique elements of my project) 
-	In the normal scenario I would prefer to use available libraries  

Details of the files in GitHub : 
-	Datafile.py – is the file which is cover both the requirements. 
-	Nypd-arrest-data-2018-1.csv – is the given source data file 
-	Output.csv – is the output file post completing the requirement 2 
-	Test_process_data.py – is the unit test file

Contact
Created by @Sree - feel free to contact me!






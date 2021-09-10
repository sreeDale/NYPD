import csv

filename='C:/NYPD/nypd-arrest-data-2018-1.csv'
outputfile='C:/NYPD/output.csv'
fields=[]
rows=[]
with open(filename,'r') as csv_file, open(outputfile,'w') as outputfilewriter:
                cvs_reader=csv.reader(csv_file)
                cvs_writer=csv.writer(outputfilewriter)
            
                fields = next(cvs_reader)               
                uvalue=input("Enter your value :") 
                print(uvalue)
             

                for row in cvs_reader:
                    for fields in row :
                        if fields==uvalue:
                           print((row))
                           #cvs_writer.write(row)
                           cvs_writer.writerow(row)
                           print("open the file and look for the")
                           break 
        
                         #for row in rows[:5]:
                # print(row)
                
            
            
            
    

                 
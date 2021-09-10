import csv
from itertools import islice


class SampleDataProcessing:


    def calc_pos_column( header , column_name):
        curr_posn=0
        for i in header:
            if i==column_name:
               return curr_posn
            else:
               curr_posn =curr_posn + 1

    def read_csv_rawdata(self,myfile):
        dict_of_offense_desc = {}
        with open(myfile) as csv_file:
            cvs_reader=csv.reader(csv_file)
            line_count=0
            for row in cvs_reader:
                if line_count ==0:
                    print(row)
                    column_posn=SampleDataProcessing.calc_pos_column(row,'OFNS_DESC')
                    print('position of the column list'+ str(column_posn))
                else:
                    if row[column_posn] not in dict_of_offense_desc:
                        dict_of_offense_desc[row[column_posn]] = 1
                    else:
                        dict_of_offense_desc[row[column_posn]]+=1

                line_count+=1

        sorted_dict_of_offence_desc = {k: v for k, v in sorted(dict_of_offense_desc.items(), key=lambda item: item[1],
                                                               reverse=True)}
        
        return sorted_dict_of_offence_desc



if __name__ == "__main__":
    read_and_count = SampleDataProcessing()

    read_file = read_and_count.read_csv_rawdata('C:/NYPD/nypd-arrest-data-2018-1.csv')
    dict_items = read_file.items()
    print(" Requiremt :Produce a dictionary count records group by OFNS_DESC in descending order ")
    print("-----------------------------------------------------------------------")
    first_10= list(dict_items)[:10]
    iterator=islice(first_10,10)
    for item in iterator:
     print(item)
    print("---------------------------------------------------------------------------") 
    print("list of Offense descriptions")
    for str in dict_items:
        print(str)
#offense_desc=input("Enter Offense description")
#print(offense_desc)
 
    
 



























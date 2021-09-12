import csv


class SampleDataProcessing:
    import csv

    def calc_posn_of_column(header, column_name):
        curr_posn = 0
        for i in header:
            if i == column_name:
                return curr_posn
            else:
                curr_posn += 1

    def read_csv(self, my_file, grouping_column):
        dict_of_offence_desc = {}
        with open(my_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(row)
                    column_posn = SampleDataProcessing.calc_posn_of_column(row, grouping_column)
                 #   print('position of column is:' + str(column_posn))
                else:
                    if row[column_posn] not in dict_of_offence_desc:
                        dict_of_offence_desc[row[column_posn]] = 1
                    else:
                        dict_of_offence_desc[row[column_posn]] += 1

                line_count += 1
        sorted_dict_of_offence_desc = {k: v for k, v in sorted(dict_of_offence_desc.items(), key=lambda item: item[1],
                                                               reverse=True)}

        return sorted_dict_of_offence_desc

    def write_to_csv(self, input_file, output_file, lookup_column, keyword):
        with open(input_file) as csv_file, open(output_file, 'w', newline="") as file:
            csv_reader = csv.reader(csv_file)
            writer = csv.writer(file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                   # print(row)
                    column_posn = SampleDataProcessing.calc_posn_of_column(row, lookup_column)
                    writer.writerow(row)
                else:
                    if keyword in row[column_posn]:
                        writer.writerow(row)
                line_count += 1


if __name__ == '__main__':
    read_and_count = SampleDataProcessing()

    read_file = read_and_count.read_csv('C:/NYPD/nypd-arrest-data-2018-1.csv'
                                  , 'OFNS_DESC')

    dict_items = read_file.items()

    first_10 = list(dict_items)[:10]

    print(first_10)
    uvalue=input("Enter Required Offence Description Category to export to CSV  :") 
    print(uvalue)
    read_and_count.write_to_csv('C:/NYPD/nypd-arrest-data-2018-1.csv',
                                'C:/NYPD/output.csv', 'OFNS_DESC', uvalue)
    print(" For records please find the export file name output.csv")                          


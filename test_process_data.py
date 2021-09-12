import unittest
import csv
from Datafile import SampleDataProcessing as Sp


class TestDataPrep:
    def create_testfile():
        with open('test_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["col_1", "col_2", "col_3"])
            writer.writerow(["1", "A", "X"])
            writer.writerow(["1", "A", "X"])
            writer.writerow(["1", "B", "X"])
            writer.writerow(["1", "", "X"])




class MyTestCase(unittest.TestCase):
    def test_something(self):
        TestDataPrep.create_testfile()
        ######## Tesing data-defined inputs ########
        dict_1 = Sp.read_csv(self, 'test_data.csv', 'col_2')
        self.assertEqual(dict_1['A'], 2) 
        self.assertEqual(dict_1[''], 1)
        dict_2 = Sp.read_csv(self, 'test_data.csv', 'col_3')
        self.assertEqual(dict_2['X'], 4)






if __name__ == '__main__':
    unittest.main()

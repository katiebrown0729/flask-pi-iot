# Add a reading
# List readings
# Get readings for a given serial number
# Get readings for a given date/time range
#etc

import unittest
import random
import datetime as dt
from pathlib import Path
from stored_readings import StoredReadings

class TestStoredReadings(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_readings(self):
        print("Starting ADD readings test.")
        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", dt.datetime.now(), x, y, z)


        n = aSR.get_number_of_readings()
        print('n = {}'.format(n))
        # This returns the highest index
        self.assertTrue(n == 3)


    def test_list_readings(self):
        print("Starting LIST readings test.")
        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = i
            aSR.add_readings("46406064", dt.datetime.now(), x, y, z)
        aSR.list_readings()

    def test_get_first_reading(self):
        print("Starting FIRST reading test")
        aSR = StoredReadings()

        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", dt.datetime.now(), x, y, z)

        print(aSR.get_first_reading())

    def test_get_next_reading(self):
        print("Starting NEXT reading test")
        aSR = StoredReadings()
        for i in range(0, 3):
            x = i
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", dt.datetime.now(), x, y, z)
        g=aSR.get_next_reading()
        print(g)
        self.assertTrue(g['x']==1)

    def test_get_all_data_as_list(self):
        print("Starting GET ALL DATA AS LIST test")
        aSR = StoredReadings()
        for i in range(0, 3):
            x = i
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", dt.datetime.now(), x, y, z)

        adal = aSR.get_all_data_as_list()
        print("adal: {}".format(adal))
        print("type of adal: {}".format(type(adal)))
        # test the return type is a list
        self.assertTrue(type(adal) == list)
        # test the difference between the length of the list and the number of readings is 0
        lengthAdal = len(adal)
        numberReadings = aSR.get_number_of_readings()
        n = len(adal) - aSR.get_number_of_readings()
        self.assertTrue(n == 0)

    def test_excel_maker(self):
        print("We are making an excel sheet")
        aSR = StoredReadings()
        for i in range(0, 3):
            x = i
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", dt.datetime.now(), x, y, z)
        aSR.excel_maker('my_file_name')
        my_file = Path ('./my_file_name.xlsx')

        self.assertTrue(my_file.exists())

if __name__ == '__main__':
    print("Starting Tests.")
    unittest.main()



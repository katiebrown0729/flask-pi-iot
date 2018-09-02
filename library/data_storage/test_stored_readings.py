# Add a reading
# List readings
# Get readings for a given serial number
# Get readings for a given date/time range
#etc

import unittest
import datetime
import random
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
            aSR.add_readings("46406064", "faketime", x, y, z)


        n = aSR.get_number_of_readings()
        print('n = {}'.format(n))
        self.assertTrue(n == 2)


    def test_list_readings(self):
        print("Starting LIST readings test.")
        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", "11:15", x, y, z)

        print(aSR.df)

if __name__ == '__main__':
    print("Starting Tests.")
    unittest.main()
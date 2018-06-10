import unittest
import time
import datetime
import random
import pi_iot_data as pid

class test_pi_iot_data(unittest.TestCase):


    def setUp(self):
        pass

    def test_add_readings(self):
        print("Starting ADD readings test")
        aPID = pid.PiIOTData()

        # Create data to send
        for i in range (0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aPID.add_readings("46406064", datetime, x,y,z)

        n = aPID.get_number_of_readings()
        self.assertTrue(n==3)

    def test_get_readings(self):
        print("Starting GET readings test")
        aPID = pid.PiIOTData()

        # add readings to the instance
        aPID.add_readings('12356', '180603 105800', 2.0, 20.0, 2.0)
        aPID.add_readings('121212', '180603 114500', 3.0, 30.0, 3.0)

        n = aPID.get_number_of_readings()
        self.assertTrue(n==2)

        # Get readings
        gRead = aPID.get_readings()
        print(gRead)

        # Test if the data is a list
        self.assertTrue(isinstance(gRead,list))

if __name__ == '__main__':
    print("Starting Tests.")
    unittest.main()
import unittest
import accelerometer_post as ap

class test_accelerometer_post(unittest.TestCase):

    def setUp(self):
        return

    def test_get_serverlist(self):
        l=ap.get_serverlist()
        self.assertTrue(len(l) > 0)

if __name__ == '__main__':
    unittest.main()
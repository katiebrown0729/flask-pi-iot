import unittest
import accelerometer_post as ap

class test_accelerometer_post(unittest.TestCase):

    def setUp(self):
        return

    def test_get_serverlist(self):
        l=ap.get_serverlist()
        self.assertTrue(len(l) > 0)

    def test_servers(self):
        ap.test_servers()


if __name__ == '__main__':
    unittest.main()
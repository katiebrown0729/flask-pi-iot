# This class holds data collected from the raspberry pi(s)
class PiIOTData:

    def __init__(self):
        self._readings = []

    def add_readings(self, serial_no, timestamp, x, y, z):
        self._readings.append([serial_no, timestamp, x, y, z])

    def get_number_of_readings(self):
        number_of_readings=len(self._readings)
        return number_of_readings

    def get_readings(self):
        return self._readings

if __name__ == '__main__':
    test_add_reading()
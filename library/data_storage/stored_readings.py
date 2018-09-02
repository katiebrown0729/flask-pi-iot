import pandas as pd
import numpy as np

class StoredReadings():
    def __init__(self):
        self.df = []
        #empty dataframe
        self.df = pd.DataFrame(columns=['serial-no', 'timestamp', 'x', 'y', 'z'])

        print(self.df)

 # Method for add readings
    def add_readings(self, serial_no, ts, x, y, z):
        self.df = self.df.append({'serial-no': serial_no,'timestamp':ts, 'x': x, 'y':y, 'z':z}, ignore_index=True)
        #print(self.df)

    def get_number_of_readings(self):
        number_of_readings = self.df.index.max()
        return number_of_readings

if __name__ == '__main__':
    # Instantiating the class is required for this shit to run
    # Otherwise df is not recognized
    # ^ Instantiates the class
    aSR = StoredReadings()

import pandas as pd
import numpy as np

class StoredReadings():
    def __init__(self):
        self.df = []
        #empty dataframe
        self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])
     #   print(self.df)
        self.i = 0

 # Method for add readings
    def add_readings(self, serial_no, ts, x, y, z):
        self.df = self.df.append({'serial_no': serial_no,'timestamp':ts, 'x': x, 'y':y, 'z':z}, ignore_index=True)
        # To print each append data step, uncomment below.
        # print(self.df)

    def get_number_of_readings(self):
        number_of_readings = self.df.index.max()
        return number_of_readings

        def list_readings(self):
        print(self.df)

    def get_first_reading(self):
        self.i = i = 0
        d={'serial_no':self.df.serial_no[i],'timestamp':self.df.timestamp[i],'x':self.df.x[i],'y':self.df.y[i],'z':self.df.z[i]}
        return d
    
    def get_next_reading(self):
        self.i = self.i + 1
        d = {
            'serial_no': self.df.serial_no[self.i],
            'timestamp': self.df.timestamp[self.i],
            'x': self.df.x[self.i],
            'y': self.df.y[self.i],
            'z': self.df.z[self.i]
        }
        return d

    def get_intial_readings(self):
        pass

    def get_all_data_as_list(self):
        #get first
        #get next
        # how does it know when to stop?
        # use a while loop - do this until something happens
            #get  next should return an empty value when it hits the end
        #ensure self.i is not greater than get number of readings, when it is, return null

if __name__ == '__main__':
    # Instantiating the class is required for this shit to run
    # Otherwise df is not recognized
    # ^ Instantiates the class
    aSR = StoredReadings()

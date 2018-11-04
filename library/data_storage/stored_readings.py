import pandas as pd
import numpy as np


class StoredReadings():
    def __init__(self):
        self.df = []
        #empty dataframe
        self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])
     #   print(self.df)
        self.i = 0
        self.fileNumber = 0 #used for excel writer to increment filename

 # Method for add readings
    def add_readings(self, serial_no, ts, x, y, z):
        self.df = self.df.append({'serial_no': serial_no,'timestamp':ts, 'x': x, 'y':y, 'z':z}, ignore_index=True)
        # To print each append data step, uncomment below.
        # print(self.df)
        self.readings_saver()

    def get_number_of_readings(self):
        number_of_readings = self.df.index.max() + 1
        return number_of_readings

    def list_readings(self):
        print(self.df)

    def get_first_reading(self):
        sizeOfDataFrame = self.df.shape[0]
        if sizeOfDataFrame > 0:
            self.i = i = 0
            d={'serial_no':self.df.serial_no[i],'timestamp':self.df.timestamp[i],'x':self.df.x[i],'y':self.df.y[i],'z':self.df.z[i]}

        else:
            d={'serial_no':"None",'timestamp':"None",'x':0,'y':0,'z':0}

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
        print("d is {}".format(d))
        return d

    def get_intial_readings(self):
        pass

    def get_all_data_as_list(self):
        datalist = []
        # get first
        first = self.get_first_reading()
        # print("first: {}".format(first))
        datalist.append(first)
        # print("datalist: {}".format(datalist))
        #get next

        # how does it know when to stop?
        # use a while loop - do this until something happens
            #get  next should return an empty value when it hits the end
        #ensure self.i is not greater than get number of readings, when it is, return null
        while True:
            try:
                somethingelse = self.get_next_reading()
                datalist.append(somethingelse)
            except Exception as ex:
                #print("We got an unexpected error {}.".format(ex))
                return datalist

    #def excel_maker(self, filename, dataframe):


    def readings_saver(self):
        n = self.get_number_of_readings()
        if n>=1000:
            self.fileNumber = self.fileNumber +1
            filename = 'Saved Readings' + str(self.fileNumber) + '.xlsx'
            print('Saving the last 1000 readings to {}'.format(filename))
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            self.df.to_excel(writer, sheet_name='accelData')
            writer.save()
            self.df = []
            self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])



if __name__ == '__main__':
    # Instantiating the class is required for this shit to run
    # Otherwise df is not recognized
    # ^ Instantiates the class
    aSR = StoredReadings()

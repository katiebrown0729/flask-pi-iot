import pandas as pd
import boto3
import numpy as np
import sqlite3
import random
import datetime as dt


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
        #self.readings_saver()
        self.aws_readings_saver()

# Method for adding readings to dataframe
    def create_dataframe_for_testing(self):
        print("Create dataframe for testing.")
        # Create an empty dataframe
        incoming_df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])

        # Create data for dataframe
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            d = dt.datetime.now()
            sn = "46406064"
            incoming_df = incoming_df.append({'serial_no': sn, 'timestamp': d, 'x': x, 'y': y, 'z': z}, ignore_index=True)

        return incoming_df

    def df_to_list_of_dicts(self, df):
        datalist = []

        for i, row in df.iterrows():
            #print('The row is: {}'.format(row))
            print("this is the serial from row {}".format(row.serial_no))
            d={'serial_no':row.serial_no,'timestamp':row.timestamp,'x':row.x,'y':row.y,'z':row.z}
            datalist.append(d)

        return(datalist)


#DB is throwing DB BS into this code. KT disapproves.
    def add_readings_to_db(self, serial_no, ts, x, y, z):
        conn = sqlite3.connect('data\\readings.db')
        cur = conn.cursor()
        sql_string = "insert into readings (x, y, z, serial_no, timestamp) values ('{0}','{1}','{2}','{3}','{4}');".format(x, y, z, serial_no, ts)
        cur.execute(sql_string)
        conn.commit()
        conn.close()

    def get_number_of_readings(self):
        number_of_readings = self.df.index.max() + 1
        return number_of_readings

    def get_number_of_readings_from_db(self):
        conn = sqlite3.connect('data\\readings.db')
        cur = conn.cursor()
        cur.execute('select count(*) from readings;')
        result = cur.fetchall()
        count = result[0][0]
        conn.commit()
        conn.close()
        return count

    def get_df_from_db_by_serial_no(self, serial_no):
        conn = sqlite3.connect('data\\readings.db')
        #serial_input = input('Enter serial no. ')
        sqlString = 'select * from readings where serial_no = "{}"'.format(serial_no)
        print(sqlString)
        df = pd.read_sql_query(sqlString, conn)
        return df

    def get_unique_serial_no_from_db(self):
        conn = sqlite3.connect('data\\readings.db')
        cur = conn.cursor()
        cur.execute('select distinct(readings.serial_no) from readings;')
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

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
        # Ensure .append does what you are expecting
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
            filename = 'Saved_Readings_' + str(self.fileNumber) + '.xlsx'
            print('Saving the last 1000 readings to {}'.format(filename))
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            self.df.to_excel(writer, sheet_name='accelData')
            writer.save()
            self.df = []
            self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])
            s3 = boto3.resource('s3')
            s3.meta.client.upload_file(filename, 'katiefirstbuckettest', filename)

    def aws_readings_saver(self):
        bucket = "katiefirstbuckettest"
        n = self.get_number_of_readings()
        if n >= 1000:
            self.fileNumber = self.fileNumber + 1
            filename = 'Saved_Readings_' + str(self.fileNumber) + '.csv'
            data_string = self.df.to_csv()
            s3 = boto3.resource('s3')
            s3.Bucket(bucket).put_object(Key=filename, Body=data_string)
            #Resetting the dataframe
            self.df = []
            self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])


if __name__ == '__main__':
    # Instantiating the class is required for this shit to run
    # Otherwise df is not recognized
    # ^ Instantiates the class
    aSR = StoredReadings()

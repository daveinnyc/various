#################################################################wget
# import_traffic_data.py
#
# Clean up traffic data downloaded from:
#    https://catalog.data.gov/dataset/traffic-violations-56dda/
#             resource/450018e7-f6c0-43fd-b5c9-a83de293b206
#
# Create a simple sqlite3 database
# Import the cleaned up data into sqlite3
#
# Copyright 2017, Dave Cuthbert
# License: MIT
##################################################################
import re
import sqlite3
import os 
import datetime

DATABASE = "traffic_stops.db"
CSV_INPUT = "traffic.csv"
#CSV_INPUT = "test.csv"
EXPECTED_FIELDS_COUNT = 39


def create_fresh_db(DATABASE):
   if os.path.exists(DATABASE):
      os.remove(DATABASE)

   empty_db = open(DATABASE, 'a')
   empty_db.close()
   
def connect_to_dbase(DATABASE):
   try:
      dbase_connection = sqlite3.connect(DATABASE)
      return dbase_connection
   except Exception as e:
      print "CONNECTION ERROR: ",
      print e

def create_table(connection, create_sql):
   try:
      db = connection.cursor()
      db.execute(create_sql)
   except Exception as e:
      print "CREATE TABLE ERROR: ",
      print e
  
def create_table_alldata(connection):

   create_table_alldata = """ CREATE TABLE IF NOT EXISTS alldata
                             (id integer PRIMARY KEY NOT NULL, 
                              DateOfStop text,
                              TimeOfStop text,
                              Agency text,
                              SubAgency text,
                              Description text,
                              Location text,
                              Latitude text,
                              Longitude text,
                              Accident integer,
                              Belts integer,
                              PersonalInjury integer,
                              PropertyDamage integer,
                              Fatal integer,
                              CommercialLicense integer,
                              HAZMAT integer,
                              CommercialVehicle integer,
                              Alcohol integer,
                              WorkZone integer,
                              State text,
                              VehicleType text,
                              Year integer,
                              Make text,
                              Model text,
                              Color text,
                              ViolationType text,
                              Charge text,
                              Article text,
                              ContributedToAccident text,
                              Race text,
                              Gender text,
                              DriverCity text,
                              DriverState text,
                              DLState text,
                              ArrestType text,
                              Geolocation text,
                              YearOfStop integer,
                              MonthOfStop integer,
                              DayOfStop integer,
                              DayNameOfStop text  
                             ); """  

   try:
      create_table(connection, create_table_alldata)
   except Exception as e:
      print "CREATE TABLE ERROR: ",
      print e


def parse_date(date_of_stop_field):
    month, day, year = date_of_stop_field.split('/')
    day_of_week = datetime.date(int(year), int(month), int(day)).weekday()
   
    return "," + year + "," + month + "," + day + "," + str(day_of_week)


def parse_row(row):
   embedded_comma = re.compile("(,\")(\w.*?),(.*?)(\"),")
   geo_coordinates = re.compile("(\")(\(.*?),(.*?\))(\")")
   date_of_stop_field = re.compile("(\d\d)/(\d\d)/(\d\d\d\d)")               

   row = re.sub("\n", "", row)                                         # Drop line break from row
   
   with_commas  = re.search(embedded_comma, row)                        # Find fields with internal commas
   while(with_commas):
      if (with_commas):                                                  
         without_commas = with_commas.group(0).replace(",", "")          # Remove internal commas
         without_commas = "," + without_commas.replace("\"", "") + ","   # Drop the quotes, return field separator
         row = row.replace(with_commas.group(0), without_commas)
      with_commas  = re.search(embedded_comma, row)                     # Check for more quoted fields with commas
   
   replacement = re.search(geo_coordinates, row)                        # Fix geo coordinate pairs
   while (replacement):
      row = re.sub(geo_coordinates, replacement.group(2) + "," 
                    + replacement.group(3), row, count=1)
      replacement = ''
   
   date_of_stop = re.search(date_of_stop_field, row) 
   if date_of_stop:
      row = row + parse_date(date_of_stop.group(0))                    # Give rows more date precision
   else:
      row = row + ",,,,"                                               # Keep number of fields consistent

   return row     


def set_fake_booleans(list_of_values):
   for idx, v in enumerate(list_of_values):
      if 'No' == v:
         list_of_values[idx] = 0
      if 'Yes' == v:
         list_of_values[idx] = 1

   return list_of_values    
      

def insert_row_alldata(connector, row):
   insert_sql = '''INSERT INTO alldata (DateOfStop, TimeOfStop, Agency, SubAgency, Description,
                         Location, Latitude, Longitude, Accident, Belts, PersonalInjury, 
                         PropertyDamage, Fatal, CommercialLicense, HAZMAT, CommercialVehicle, Alcohol,
                         WorkZone, State, VehicleType, Year, Make, Model, Color, ViolationType, Charge,
                         Article, ContributedToAccident, Race, Gender, DriverCity, DriverState, DLState,
                         ArrestType, Geolocation, YearOfStop, MonthOfStop, DayOfStop, DayNameOfStop
                   ) VALUES (?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, 
                             ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, 
                             ?,?,?,?,?, ?,?,?,?)
                '''
   try:
      connector.execute(insert_sql, row)
   except sqlite3.Error as e:
      print "INSERT ERROR: ",
      print e

        
def clean_and_load_data(connector, CSV_INPUT):
   try:
      input_file = open(CSV_INPUT, "r")
   except Exception as e:
      print "CONNECT ERROR: ",
      print e

   row_counter = 0
   for row in input_file.readlines():
      parsed_row = parse_row(row) 
      row = parsed_row.split(",")                         # Can split the final geo coordinate field
      if len(row) == (EXPECTED_FIELDS_COUNT + 1):         # Fix geo coordinates if split apart
         row[34] = str(row[34]) + "," + str(row[35])
         del row[35]
      row_fields = set_fake_booleans(row)

      if len(row) != EXPECTED_FIELDS_COUNT:               # Check number of fields and load if ok
         print "FIELD COUNT ERROR: " + str(row)
      else:
         insert_row_alldata(connector, row)
         row_counter += 1
         if ((row_counter % 100) == 0):
            connector.commit()
   connector.commit()
 

def main():
   create_fresh_db(DATABASE)
   db = connect_to_dbase(DATABASE)
   create_table_alldata(db)
   clean_and_load_data(db, CSV_INPUT)

if "__main__" == __name__:
   main()

#EOF

from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import json

f = open('./geocode_data/upazillas.json')
data = json.load(f)


try:
  cnx = mysql.connector.connect(user='sanjib', password='Pass4@Admin#', host='127.0.0.1', database='geocode_db')
  if cnx and cnx.is_connected():
      print(f"Connection successful")
      cursor = cnx.cursor()
      result = cursor.execute("SELECT * FROM upazilas WHERE district_id in (SELECT id FROM districts WHERE division_id in (SELECT id FROM divisions WHERE name = 'Khulna'))")
      rows = cursor.fetchall()
      matched_unions = []
      count = 0
      for row in rows:
        # print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
        for upazilla in data:
            if (row[2].lower() == upazilla['name'].lower()):
                updated_upazilla = cursor.execute(f"UPDATE upazilas SET code = '{upazilla['geo_code']}' WHERE district_id = {row[1]} and name = '{upazilla['name'].lower()}'")
      cursor.execute(f"SELECT  * FROM upazilas WHERE district_id in (SELECT id FROM districts WHERE division_id in (SELECT id FROM divisions WHERE name = 'Khulna')) and code <> ''")
      updated_rows = cursor.fetchall()
      for updated_row in updated_rows:
        print(f"Updated row {updated_row}")
        #   print(f"{updated_row[0]}, {updated_row[1]}, {updated_row[2]}, {updated_row[3]}, {updated_row[5]}")
  cnx.commit()
  cursor.close()
  cnx.close()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

f.close()
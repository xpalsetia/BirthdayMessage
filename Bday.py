import csv
from datetime import datetime
import subprocess



def getPersonBirthday(file_path, column_2_value):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1]==column_2_value:
                return row[0]
            

def wishBirthday(file_path,name):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        modified_rows = []
        for row in csv_reader:
            if row[0]==name and row[2] == "false":
                phone_number = row[3]
                message = "Happy birthday " + name + "!"
                subprocess.run(['osascript', '-e', f'tell application "Messages" to send "{message}" to buddy "{phone_number}"'])



file_path = "birthdays.csv"
column_2_value = datetime.now().strftime("%m/%d")
name = getPersonBirthday(file_path, column_2_value)
wishBirthday(file_path,name)

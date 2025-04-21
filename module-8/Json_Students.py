#William Stearns
#4-20-25
#module 8.2
#Open a JSON file and display records, and then add a record to file.


import json
from os import path
import sys


# Function to print the student records in a readable format
def print_json(pupils):
    for student in pupils:
        print(f"{student['F_Name']}, {student['L_Name']}: ID = {student['Student_ID']}, Email = {student['Email']}")




# Function to update the JSON file with the new student record
# This function takes the list of students as an argument and writes it to the file
def update_file(pupils):
   with open('student.json', 'w') as json_file:
    json.dump(pupils, json_file, 
                        indent=4,  
                        separators=(',',': '))
      
      
def main():
# Check if the file exists before trying to open it
# If it does not exist, print an error message and exit the program
    if path.exists('student.json'):
        with open('student.json', 'r') as f:
            pupils = json.load(f)
    else:
        print("File not found.")
        sys.exit()

        
    print("\nThis is the original student list:")        
    print_json(pupils)

    new_student = {
        "F_Name": "Will",
        "L_Name": "Stearns",
        "Student_ID": 99999,
        "Email": "wstearns@example.com"
    }

    pupils.append(new_student)
    print("\nThis is the updated student list:")
    print_json(pupils)

    update_file(pupils)
    print("\nThe file has been updated.\n")


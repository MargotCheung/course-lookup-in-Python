from pickle import TRUE
import csv
import pandas as pd


#cleaned_reader    已被清空的reader
#full_reader       裝滿資料的reader
#whole_csv_reader  整個csv reader架構
#read_csv()        Pandas套件


#set as "none" to display all the lines
pd.set_option('display.max_rows', None)

#read csv file
csv_reader = pd.read_csv("DB_students.csv")

#read all blocks accordingly
Id = input("Enter student id or course id: ")
if len(Id) < 5:
    Id = int(Id)
    csv_reader.set_index('course_id', inplace=True)
    print(csv_reader.loc[Id])

else:
    csv_reader.set_index('student_id', inplace=True)
    print(csv_reader.loc[Id])
    
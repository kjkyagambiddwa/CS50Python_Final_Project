'''
This code makes a simple students database system that allows the user to have a database in
form of a dictionary per student that is being appended onto a list in what can be termed as list
and dictionary comprehension. Several modules are used including the csv module that allows for
action on a comma separated version file, the os module that allows us interact with the operating
system, the regular expressions module to validate entries like the studens number,the pandas module
that is providing us with itss flexible data frames that quicken the reading of files which is an
application of File I/O, tabulate which is used in making fancy looking tables in the table format called
fancy-grid which I prefer, pyfiglet's figlet_format that has fancy ascii characters for example in
the digital font.'''

import csv
import os
import re
import pandas as pd
from tabulate import tabulate
from pyfiglet import figlet_format as fig_fmt
from statistics import mean, median, mode, variance, stdev, StatisticsError


'''Creating dynamic variables for use in the code'''
FILENAME = 'project.csv'  #To store student entries
FIELDNAMES = ['Name', 'Students_no', 'Math', 'English', 'Math_lec_att', 'Eng_lec_att']


''' Appends a dictionary of a student onto a list called students'''
def add_students():
    print("\n🔹 Add Student Record 🔹")
    try:
        count = int(input("How many students do you want to add? "))
    except ValueError:
        print("❌ Invalid number. ❌")
        return

    students = [] #student list
    cnt_std = int(0)

    for _ in range(count):
        try:
            student = {
                'Name': input("Name: ").strip().capitalize(),
                'Students_no': input("Student Number (230071####): ").strip(),
                'Math': int(input("Math Marks: ")),
                'English': int(input("English Marks: ")),
                'Math_lec_att': int(input("Math Lecture Attendance (%): ")),
                'Eng_lec_att': int(input("English Lecture Attendance (%): "))
            } #iteration to enter student details in a dictionary

            #Using regular expressions to validate the students number and validating the marks
            pattern  = r"^230071[0-9]{4}$"
            match = re.search(pattern, student['Students_no'])
            if not 0<=student['Math']<=100 or not 0<=student['English']<=100:
                print("❗Invalid Math or English Marks. Should be from 0 to 100 ❗")
                continue
            if not 0<=int(student['Math_lec_att'])<=100 or not 0<=int(student['Eng_lec_att'])<=100:
                print("❗Input the attendence as a percentage from 0 to 100❗")
                continue
            if match:
                cnt_std += 1
                students.append(student) #appending the dictionary to the list
            else:
                print("❗Invalid Students Number❗")
                continue

        except ValueError:
            print("❌ Invalid entry. Skipping student. Ensure that the marks are digits❌")

    #Checking existence of the file using the os module by checking either the path or its size
    file_empty = not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0

    #Using a dictwriter to append onto the project.csv file
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if file_empty:
            writer.writeheader() #appends the specified field names in case the file is empty
        writer.writerows(students)
    if int(cnt_std) != 0:
        print(f"✅ {cnt_std} student(s) added successfully. ✅")
    else:
        print(f"❌ {int(count) - int(cnt_std)} student(s) added. ❌")



'''Deletes a student if both the student number and the name are matching utilizing the mask technique
that returns a boolean expression of either True to keep or False to Delete. If both match, df = df[Mask]
shall return False to keeping the row and hence it shall be filtered out and deleted'''
def delete_student():
    try:
        df = pd.read_csv(FILENAME, dtype = str)          #Reading the CSV as a string to avoid mismatches
        df.index = range(1, len(df) + 1)    #Ensuring that the pandas index starts from 1 instead of a 0
    except FileNotFoundError:
        print("❌ No student data file found. ❌")
        return

    #Displaying the entire database to help match which student to delete
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    name = input("Enter student Name (exact): ").strip()
    student_no = input("Enter student Number (exact): ").strip()

    #ensuring that both the conditions are met
    mask = (df['Name'].str.lower() == name.lower()) & (df['Students_no'] == student_no)

    #Confirmation before deleting if match exists
    if mask.any():
        confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
        if confirm == 'y' or confirm == 'yes':
            df = df[~mask]
            df.to_csv(FILENAME, index=False)
            print(f"✅ Student: '{name}' with student's number: '{student_no}' deleted successfully. ✅")
        else:
            print("❌ Deletion canceled. ❌")
    else:
        print("❌ No matching student found. ❌")


'''Ordering the tabular output in either ascendng or descending order'''
def asc_desc():
    while True:
        print("\n🔛 Select the order 🔛")
        print("1.Ascending 🇦-z")
        print("2.Descending z-a")
        print("3.Back 🔙")
        try:
            subopt = input("Choose Option: ")
            if subopt == '3':
                break
            if subopt not in ['1','2']:
                print("❗Invalid Choice❗")
                return
            return subopt
        except ValueError:
            print("❗Invalid Choice❗")
            return



'''Views the students in the system basing on different choices selected by the user either in
ascending or descending order'''
def view_students():
    while True:
        print("\n🔹 View Students 🔹")
        print("1. Sorted by Name")
        print("2. Sorted by Math Marks")
        print("3. Sorted by English Marks")
        print("4. View Specific Student")
        print("5. Back 🔙")
        opt = input("Choose option: ")  #Choosing an otpion

        try:
            df = pd.read_csv(FILENAME) #reading the csv
            df.index = range(1, len(df) + 1) #Starting the numbering from 1
        except FileNotFoundError:
            print("❌ No student data found. ❌")
            return

        #If no records exist
        if df.empty:
            print("❌ No records found. ❌")
            return

        #What to do when any of the 5 choices is picked. Tables are displayed using tabulate's fancy_grid format
        if opt == '1':
            sub_opt = asc_desc()  #order
            if sub_opt == '1':
                print(tabulate(df.sort_values(by='Name'), headers='keys', tablefmt='fancy_grid'))
            else:
                print(tabulate(df.sort_values(by='Name',ascending=False), headers='keys', tablefmt='fancy_grid'))
        elif opt == '2':
            sub_opt = asc_desc()  #order
            if sub_opt == '1':
                print(tabulate(df.sort_values(by='Math'), headers='keys', tablefmt='fancy_grid'))
            else:
                print(tabulate(df.sort_values(by='Math',ascending=False), headers='keys', tablefmt='fancy_grid'))
        elif opt == '3':
            sub_opt = asc_desc()  #order
            if sub_opt == '1':
                print(tabulate(df.sort_values(by='English'), headers='keys', tablefmt='fancy_grid'))
            else:
                print(tabulate(df.sort_values(by='English',ascending=False), headers='keys', tablefmt='fancy_grid'))
        elif opt == '4':
            key = input("Enter Student Name or Number: ").strip()
            student_df = df[(df['Name'].str.lower() == key.lower()) | (df['Students_no'] == key)]
            if not student_df.empty:
                print(tabulate(student_df, headers='keys', tablefmt='fancy_grid'))
            else:
                print("❌ Student not found. ❌")
        elif opt == '5':
            break
        else:
            print("❌ Invalid choice. ❌")


'''Utilizes the statistics module to do some descriptive statistics and displays each using the
figlet_format object in the pyfiglet class utilizing the digital font'''
def analyze_statistics():
    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        print("❌ No data file found. ❌")
        return

    if df.empty:
        print("❌ No data to analyze. ❌")
        return

    #Measures of dispersion, the measures of central tendency and the cv.
    while True:
        print("\n🔹 Analyze Statistics 🔹")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Variance")
        print("5. Standard Deviation")
        print("6. Summary Statistics")
        print("7. Coefficient of Variation")
        print("8. Pearson Correlation (Math vs English)")
        print("9. Back 🔙")
        opt = input("Choose an option: ")

        if opt == '9':
            break

        #More options do do the calculations on
        subopt = None
        if opt in ['1', '2', '3', '6']:
            print("  a. English")
            print("  b. Math")
            print("  c. Both")
            while True:
                subopt = input("  Choose subject: ").lower()
                if subopt not in ['a', 'b', 'c']:
                    return
                else:
                    break

        try:
            if opt == '1':
                if subopt == 'a':
                    print(fig_fmt(f"English Mean = {mean(df['English']):.2f}", font='digital'))
                elif subopt == 'b':
                    print(fig_fmt(f"Math Mean = {mean(df['Math']):.2f}", font='digital'))
                elif subopt == 'c':
                    print(fig_fmt(f"English Mean = {mean(df['English']):.2f} and Math Mean = {mean(df['Math']):.2f}", font='digital'))
            elif opt == '2':
                if subopt == 'a':
                    print(fig_fmt(f"English Median = {median(df['English'])}", font='digital'))
                elif subopt == 'b':
                    print(fig_fmt(f"Math Median = {median(df['Math'])}", font='digital'))
                elif subopt == 'c':
                    print(fig_fmt(f"English Median = {median(df['English'])}, Math Median = {median(df['Math'])}", font='digital'))
            elif opt == '3':
                try:
                    if subopt == 'a':
                        print(fig_fmt(f"English Mode = {mode(df['English'])}", font='digital'))
                    elif subopt == 'b':
                        print(fig_fmt(f"Math Mode = {mode(df['Math'])}", font='digital'))
                    elif subopt == 'c':
                        print(fig_fmt(f"English Mode = {mode(df['English'])} and Math Mode = {mode(df['Math'])}", font='digital'))
                except StatisticsError:
                    print("❌ No unique mode found. ❌")
            elif opt == '4':
                print(fig_fmt(f"English Variance: {variance(df['English']):.2f}, Math Variance: {variance(df['Math']):.2f}", font='digital'))
            elif opt == '5':
                print(fig_fmt(f"English Std Dev: {stdev(df['English']):.2f}, Math Std Dev: {stdev(df['Math']):.2f}", font='digital'))
            elif opt == '6':
                if subopt == 'a':
                    print(tabulate(df[['English']].describe(), headers = 'keys', tablefmt = 'fancy_grid')) #outputing a 2D pandas DataFrame
                elif subopt == 'b':
                    print(tabulate(df[['Math']].describe(), headers = 'keys', tablefmt = 'fancy_grid'))
                else:
                    print(tabulate(df[['Math', 'English']].describe(), headers = 'keys', tablefmt = 'fancy_grid'))
            elif opt == '7':
                print(fig_fmt(f"English CoV: {stdev(df['English']) / mean(df['English']):.2f}", font='digital'))
                print(fig_fmt(f"Math CoV: {stdev(df['Math']) / mean(df['Math']):.2f}", font='digital'))
            elif opt == '8':
                corr = df['Math'].corr(df['English'])
                print(fig_fmt(f"Pearson correlation (Math vs English): {corr:.2f}", font='digital'))
            else:
                print("❌ Invalid option. ❌")
        except Exception as e:
            print(f"❌ Error: {e} ❌")

'''The main function that displays the main menu and runs the entire code in a systematic flow'''
def main():
    while True:
        print("\n" + fig_fmt("Student DB", font="doom"))
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View Students")
        print("4. Analyze Statistics")
        print("5. Exit 🚫")

        choice = input("Choose option: ")

        #menu choice
        match choice:
            case '1':
                add_students()
            case '2':
                delete_student()
            case '3':
                view_students()
            case '4':
                analyze_statistics()
            case '5':
                print("👋 Exiting... 👋")
                break
            case _:
                print("❌ Invalid choice. ❌")


if __name__ == "__main__":
    main()

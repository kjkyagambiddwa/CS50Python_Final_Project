#<ins>***Student Records Management System***</ins>

####<https://www.youtube.com/watch?v=XOnWPpmvcnk>

This project is a simple Python programme to manage student records stored in a CSV file. It is supposed to take in student details and can return some descriptive statistics on the performance of the class. It allows you to add, view, delete, and analyse student pereformance using the descriptive statistics. The programme uses libraries like `pandas`, `pyfiglet`, and `tabulate` for handling data, displaying neat output, and displaying neat tables.

##***Features***

###**1. Add students**
- This function called add_student takes as input the number of students one wants to add, then the students details to add, which details it then appends them to a comma separated version (csv) file.
- You can enter details for multiple students at once. You just need to enter the number of students you want to add
at one go.
- Each student has a name, student number(that begins with 230071____ and it is followed by 4 numbers), math and English marks, and lecture attendance in percentage for both the subjects for the period before the exams.

###**2. View students**
- This is run by a function called view_students
- It can enable ou to View all saved student records in a clean tables well displayed using the tabulate module based on your choice of sorting to either sort by the name, or by the marks which can further be sorted in either ascending or descending order by another function called asc_desc.
- You can also view a specific student by entering either their name or student number.

###**3. Delete a Student**
- This is run by a function called delete_student.
- The function first displays the dataset to enable you confirm the details of the student you want to delete. You must provide both the name and student number. The function uses a mask technique to ensure that both criteria are passed and that the student's name and number match before doing the deletion.
- The programme confirms before deleting the student’s record where you can type in the different variations of yes or y and it shall accept the deletion. entries of yah, and others shall not work.

###**4. Analyse Statistics**
- This is run  by a function called analyze_statistics
- Get useful statistics like the mean(average), median, mode, and standard deviation for marks and attendance.
- Also shows maximum and minimum values.
- You can calculate the Pearson correlation between Math and English scores.
- Tables showing complete summary statistics of either English, Math or even both.

###**5. Ordering in ascending or descending order**
- This is run by a function called asc_desc.
- It works out the odering while viewing the different output for example if you decide to view students, you can decide the order you want to view it. It uses the pandas sort_values object that does the sorting with ascending either set to True of force.

###**6. Exit**
- This exits you from the program.
- It quite the program with goodbye emojis and it is used when you are done using the application.

###**7. General Functionalities**
- There are several back options that can take you to the previous options within the menu just in case you would like to use the application differently.
- They mostly utilize the break functionality to quit the existing while loops.

##***Modules Used***

- **Python**: Main programming language.
- **Pandas**: For reading and writing CSV files and carrying out data analysis on the marks.
- **Tabulate**: For displaying data in pretty tables using the personal preference format called `fancy_grid`.
- **PyFiglet**: Adds nice ASCII art titles and different specific statistics for the programme utilizing the `digital` and `doom` fonts that are also personal preferences.

##***File Structure***

- `project.csv`: This is where student data is stored.
- `main.py`: This file contains the menu and logic to run the programme.
- `project.py`: Contains the *add_students*, *delete_student*, *view_students*, *analyze_statistics*, and the *asc_desc* functions which run the program.
- `test_project.py`: Has tests written using `pytest`, `unittest.mock's patch object`  to make sure this project works correctly.

##***How to Run***

1. Make sure you have Python installed. With python comes pre-installed libraries like os, csv and the regular expressions (re)

2. Install required libraries:
   ```bash
   pip install pandas tabulate pyfiglet pytest
   ```
3. Run the programme:
   ```bash
   python project.py
   ```

##***How to Test***

To run the tests and check if everything works:
```bash
pytest test_project.py
```

This will show which parts are working and if there are any errors.

##***Note!***

- The programme is designed to be simple and easy to use.
- Data is saved in a local file, so it will remain even after the programme is closed.
- Warnings may show up during tests if only one student is added (correlation needs two students).


##***Sample Output***

![alt text](image.png)

# Timetable_Management
Student timetable management system

Student Timetable Management System

About the Project

This is a simple Python-based Student Timetable Management System made to organize and manage weekly class schedules.

The main idea behind this project is to make a timetable easier to handle instead of keeping all the class details separately. The program allows the user to add classes, view the complete timetable, find clashes, remove duplicate entries, and get some useful information about the weekly schedule.

I have also tried to use the programming concepts covered in our modules, such as functions, tuples, lists, dictionaries, loops, conditional statements, counting, swapping, sorting, partitioning and reversal.

Features

- Add a new class to a particular day
- Store subject, start time, end time and class type
- View the complete weekly timetable
- View the timetable in reverse day order
- Check for classes having the same starting time
- Remove accidentally repeated class entries
- Find the busiest day of the week
- Count how many classes are conducted for each subject
- Swap two periods between days
- Separate Theory and Lab classes for a selected day
- Find the Kth least busy day
- Run basic verification checks

How the Program Works

When the program starts, a menu with different options is displayed.

The user can select an option by entering its number. For example, if the user selects Add a class, the program asks for:

- Day
- Subject
- Starting time
- Ending time
- Class type (Theory/Lab)

The entered information is stored as a tuple inside the timetable.

The program keeps separate lists for each day from Monday to Saturday, which makes it easier to add and display classes.

Programming Concepts Used

1. Functions

Different tasks are divided into separate functions such as:

- "add_class()"
- "check_clashes()"
- "remove_duplicate_entries()"
- "busiest_day()"
- "subject_wise_count()"
- "swap_periods()"
- "view_timetable()"

This keeps the program organized and makes individual parts easier to understand.

2. Lists, Tuples and Dictionaries

A dictionary is used to store the timetable day-wise.

Each class is stored as a tuple containing:

"(subject, start_time, end_time, class_type)"

For example:

"("Python", "09:00", "10:00", "Theory")"

3. Loops and Conditions

"for" and "while" loops are used for displaying classes, counting subjects, checking clashes and running the menu continuously.

"if-elif-else" conditions are used to handle different menu choices.

4. Counting

The program counts:

- Number of periods on each day
- Number of classes for each subject

This information is also used to find the busiest and least busy days.

5. Swapping

The "swap_periods()" function demonstrates exchange of values by swapping two timetable entries.

6. Sorting

The Kth least busy day feature uses a simple bubble-sort style approach to arrange days according to their number of periods.

7. Partitioning

The "partition_theory_lab()" function separates classes into two groups:

- Theory
- Lab

This makes it easier to see the type of classes scheduled on a particular day.

8. Reversal

The timetable can also be displayed in reverse day order using list slicing.

Example of Stored Data

A class entry is stored like this:

("Mathematics", "09:00", "10:00", "Theory")

Multiple entries are stored under their respective days.

For example:

Monday:
    Mathematics
    Python
    Physics Lab

Menu Options

1. Add a class
2. View timetable
3. View timetable (reverse day order)
4. Check for clashes
5. Remove duplicate entries
6. Show busiest day
7. Show subject-wise class count
8. Swap two periods
9. Partition a day into Theory and Lab classes
10. Find Kth least busy day
11. Run verification checks
12. Exit

Verification

A basic verification function is included in the project.

It checks the number of timetable entries before and after duplicate removal. The purpose is to make sure that the duplicate-removal operation is working as expected and is not increasing the number of entries.

Project Structure

Student-Timetable-Management-System/
│
├── timetable.py
└── README.md

Sample Output

------ Student Timetable Management System ------

1. Add a class
2. View timetable
3. View timetable (reverse day order)
4. Check for clashes
5. Remove duplicate entries
6. Show busiest day
7. Show subject-wise class count
8. Swap two periods
9. Partition a day into Theory and Lab classes
10. Find Kth least busy day
11. Run verification checks
12. Exit

After adding classes, the timetable can be displayed day-wise:

Monday:
  09:00-10:00  Mathematics  (Theory)
  10:00-11:00  Python  (Theory)

Tuesday:
  11:00-12:00  Physics Lab  (Lab)

What I Learned From This Project

While making this project, I got practice with storing data using lists, tuples and dictionaries and also understood how functions can be used to divide a larger problem into smaller parts.

I also got to apply basic algorithms such as counting, swapping, sorting, duplicate removal and partitioning in one project instead of using them only as separate examples.

The project helped me understand how different programming concepts can be combined to make a small but functional application.

Conclusion

The Student Timetable Management System is a console-based Python project designed to manage a student's weekly timetable.

It combines basic Python programming with fundamental problem-solving and algorithmic techniques. The project can also be extended in the future by adding features such as editing or deleting classes, checking complete time-range overlaps, saving the timetable permanently, or adding a graphical interface.


AUTHOR 
saroj Rajpurohit


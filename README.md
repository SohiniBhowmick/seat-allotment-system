Examination Seating Arrangement System

A Python-based project that automatically allocates examination seats to students from multiple sections using predefined rules and seating constraints.

Project Overview

The Examination Seating Arrangement System is designed to simplify the process of allocating students to examination rooms and seats.

The system checks room capacity, organizes students, applies seating constraints, assigns seats, and generates room-wise seating arrangements.

It also allows users to search for a student's seating details using their roll number.

This project uses basic Python programming concepts and built-in data structures. It does not require AI/ML, databases, recursion, or external libraries.

Key Features

- Student information management
- Examination room and capacity management
- Automatic seat allocation
- Section separation between adjacent seats
- Subject separation between adjacent seats
- Preferred room allocation
- Priority seating for students with special requirements
- Unique student and seat allocation
- Room-wise seating arrangement
- Invigilator information display
- Student seat lookup using roll number
- Room-wise summary generation
- Validation of seating constraints
- Reproducible seating arrangements

Seating Rules

The system follows these predefined rules:

1. Section Separation: Students from the same section should not occupy adjacent seats.
2. Subject Separation: Students appearing for the same subject should not occupy adjacent seats.
3. Room Capacity: The number of students assigned to a room must not exceed its capacity.
4. Unique Student Allocation: Every eligible student must receive exactly one seat.
5. Unique Seat Allocation: A seat cannot be assigned to more than one student.
6. Preferred Room Constraint: Students should be assigned to their preferred room whenever a valid seat is available.
7. Special Requirement Constraint: Students with special requirements receive priority seats.
8. Invigilator Information: Each room displays its assigned invigilator's name.
9. Reproducibility: The same input and rules produce the same seating arrangement.

Required Functions

The program includes separate functions for major operations, such as:

- "add_student()"
- "remove_student()"
- "display_students()"
- "validate_students()"
- "calculate_room_capacity()"
- "check_capacity()"
- "group_students()"
- "arrange_students()"
- "assign_seats()"
- "display_seating_plan()"
- "search_student()"
- "find_student_seat()"
- "generate_room_summary()"

Minimum Test Dataset

The project should be tested using at least:

- 24 students
- 4 different sections
- 4 different examination subjects
- 4 examination rooms
- At least 2 students with preferred rooms
- At least 2 students with special requirements

Project Structure

Examination-Seating-Arrangement-System/
│
├── main.py
│
└── README.md

Requirements

- Python 3.8 or later
- VS Code or any Python-supported IDE
- No external package installation required

How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

python main.py

4. Follow the menu instructions to manage students and generate the seating arrangement.

Python Concepts Demonstrated

This project demonstrates the following Python concepts:

- Variables and data types
- Conditional statements ("if", "elif", "else")
- Loops ("for" and "while")
- Lists and dictionaries
- User-defined functions
- Function arguments and return values
- Sorting and grouping
- String handling
- Input validation
- Logical operators
- Searching techniques
- Rule-based allocation
- Basic problem-solving techniques

Important Notes

- Each student must receive only one examination seat.
- No two students can occupy the same seat.
- Room capacity must always be respected.
- Seating constraints must be checked before finalizing the arrangement.
- The system uses deterministic allocation rather than random seat assignment.

Future Improvements

- Add a graphical user interface (GUI).
- Add permanent student and room data storage.
- Export seating arrangements as PDF files.
- Generate printable student-wise seating slips.
- Add an administrative dashboard.

---

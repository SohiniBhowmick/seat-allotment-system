# Examination Seating Arrangement System

# Student Data
students = []

names = [
    "Rahul", "Priya", "Ritam", "Sneha",
    "Rohan", "Anjali", "Riya", "Raj",
    "Karan", "Neha", "Suman", "Puja",
    "Ayan", "Isha", "Ravi", "Tina",
    "Sahil", "Moumita", "Akash", "Diya",
    "Aditya", "Payel", "Sourav", "Nisha"
]

sections = ["A", "B", "C", "D"]
subjects = ["Python", "DBMS", "DSA", "Networking"]

# Create 24 students
for i in range(24):
    student = {
        "roll": 101 + i,
        "name": names[i],
        "section": sections[i % 4],
        "subject": subjects[i % 4],
        "preferred": "",
        "special": False,
        "room": "",
        "seat": 0
    }

    students.append(student)

# Preferred rooms
students[0]["preferred"] = "R1"
students[7]["preferred"] = "R2"

# Special requirement students
students[2]["special"] = True
students[13]["special"] = True


# Room Information
rooms = {
    "R1": {
        "capacity": 6,
        "invigilator": "Mr. Ritam ",
        "priority": [1, 6],
        "seats": {}
    },

    "R2": {
        "capacity": 6,
        "invigilator": "Ms. Priya",
        "priority": [1, 6],
        "seats": {}
    },

    "R3": {
        "capacity": 6,
        "invigilator": "Mr. Rahul",
        "priority": [1, 6],
        "seats": {}
    },

    "R4": {
        "capacity": 6,
        "invigilator": "Ms. Sneha",
        "priority": [1, 6],
        "seats": {}
    }
}

 
# 1. Add Student
def add_student():
    # Check capacity before accepting new student
    if len(students) >= calculate_room_capacity():
        print("\nError: Maximum capacity reached!")
        print("Student cannot be added.")
        return

    roll = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists.")
            return

    name = input("Enter student name: ")
    section = input("Enter section (A/B/C/D): ").upper()
    subject = input("Enter subject: ")

    preferred = input(
        "Enter preferred room (R1-R4) or press Enter: "
    ).upper()

    special = input("Special requirement? (yes/no): ").lower()

    if section not in sections:
        print("Invalid section.")
        return

    if preferred and preferred not in rooms:
        print("Invalid preferred room.")
        return

    student = {
        "roll": roll,
        "name": name,
        "section": section,
        "subject": subject,
        "preferred": preferred,
        "special": special == "yes",
        "room": "",
        "seat": 0
    }

    students.append(student)

    # Attempt allocation
    if assign_seats():
        print("Student added successfully.")

    else:
        # Roll back new student
        students.remove(student)
        print("Student could not be added.")
        print("Existing student records are preserved.")


# 2. Remove Student
def remove_student():
    roll = int(input("Enter roll number to remove: "))

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student removed successfully.")
            return

    print("Student not found.")


# 3. Display Students
def display_students():
    print("\nSTUDENT DETAILS")
    print("-" * 65)

    for s in students:
        print(s["roll"], s["name"], s["section"],
              s["subject"], s["preferred"], s["special"])


# 4. Validate Students
def validate_students():
    valid = True

    for s in students:
        if s["roll"] <= 0 or s["name"] == "":
            valid = False

        if s["section"] not in sections:
            valid = False

    return valid


# 5. Calculate Total Room Capacity
def calculate_room_capacity():
    total = 0

    for r in rooms:
        total += rooms[r]["capacity"]

    return total


# 6. Check Capacity
def check_capacity():
    total_capacity = calculate_room_capacity()

    print("Total Students:", len(students))
    print("Total Room Capacity:", total_capacity)

    if len(students) <= total_capacity:
        print("Capacity is sufficient.")
        return True
    else:
        print("Not enough examination seats.")
        return False


# 7. Group Students
def group_students():
    return sorted(students, key=lambda s: (not s["special"], s["roll"]))


# 8. Check Seating Constraints
def check_seating(room, seat, student,seat_map):

    if seat in seat_map[room]:
        return False

    # Check adjacent seats
    for adjacent in [seat - 1, seat + 1]:

        if adjacent in seat_map[room]:

            other = seat_map[room][adjacent]

            if (other["section"] == student["section"] or
                    other["subject"] == student["subject"]):
                return False

    return True


# 9. Assign Seats
def assign_seats():
    total_capacity = calculate_room_capacity()

    # Check maximum capacity first
    if len(students) > total_capacity:
        print("Error: Maximum room capacity exceeded!")
        return False

    # Temporary seating arrangement
    new_seats = {r: {} for r in rooms}

    ordered = sorted(
        students,
        key=lambda s: (not s["special"], s["roll"])
    )


    # Backtracking allocation
    def allocate(index):

        if index == len(ordered):
            return True

        student = ordered[index]

        # Preferred room first
        if student["preferred"] in rooms:
            room_list = [student["preferred"]]

            room_list += [
                r for r in rooms if r != student["preferred"]
            ]
        else:
            room_list = sorted(
                rooms,
                key=lambda r: len(new_seats[r])
            )

        for room in room_list:

            capacity = rooms[room]["capacity"]

            if student["special"]:

                # Special students must use priority seats
                seat_list = rooms[room]["priority"]

            else:
                seat_list = list(range(1, capacity + 1))

            for seat in seat_list:

                if len(new_seats[room]) >= capacity:
                    continue

                if check_seating(room, seat, student, new_seats):

                    # Temporarily allocate seat
                    new_seats[room][seat] = student

                    if allocate(index + 1):
                        return True

                    # Backtrack if allocation fails
                    del new_seats[room][seat]

        return False

    # Try complete allocation
    if not allocate(0):

        print("Error: Valid seating arrangement not possible.")
        print("Previous seating arrangement has been preserved.")
        return False

    # Commit allocation only after complete success
    for room in rooms:
        rooms[room]["seats"] = new_seats[room]

    for room in rooms:
        for seat, student in rooms[room]["seats"].items():

            student["room"] = room
            student["seat"] = seat

    print("\nSeat allocation completed successfully.")
    return True



# 10. Validate Final Seating
def validate_final():

    allocated = set()

    for room in rooms:

        seats = rooms[room]["seats"]

        if len(seats) > rooms[room]["capacity"]:
            return False

        for seat, student in seats.items():

            key = student["roll"]

            if key in allocated:
                return False

            allocated.add(key)

            if student["special"]:
                if seat not in rooms[room]["priority"]:
                    return False

            for adjacent in [seat - 1, seat + 1]:

                if adjacent in seats:

                    other = seats[adjacent]

                    if (student["section"] == other["section"] or
                            student["subject"] == other["subject"]):
                        return False

    return len(allocated) == len(students)


# 11. Display Seating Plan
def display_seating_plan():

    for room in rooms:

        print("\nROOM:", room)
        print("Invigilator:", rooms[room]["invigilator"])
        print("-" * 65)

        print("Seat | Roll | Name | Section | Subject | Special")

        for seat in sorted(rooms[room]["seats"]):

            s = rooms[room]["seats"][seat]

            print(seat, "|", s["roll"], "|", s["name"],
                  "|", s["section"], "|", s["subject"],
                  "|", s["special"])


# 12. Search Student
def search_student():

    roll = int(input("\nEnter student roll number: "))

    for s in students:

        if s["roll"] == roll:

            print("\nSTUDENT FOUND")
            print("Name:", s["name"])
            print("Section:", s["section"])
            print("Subject:", s["subject"])
            print("Examination Room:", s["room"])
            print("Seat Number:", s["seat"])
            return

    print("Student not found.")


# 13. Find Student Seat
def find_student_seat():
    search_student()


# 14. Generate Room Summary
def generate_room_summary():

    print("\nROOM-WISE SUMMARY")
    print("-" * 45)

    for room in rooms:

        occupied = len(rooms[room]["seats"])
        capacity = rooms[room]["capacity"]

        print("\nRoom:", room)
        print("Invigilator:", rooms[room]["invigilator"])
        print("Capacity:", capacity)
        print("Occupied Seats:", occupied)
        print("Available Seats:", capacity - occupied)


# Main Program
print("=" * 55)
print(" EXAMINATION SEATING ARRANGEMENT SYSTEM ")
print("=" * 55)

if validate_students() and check_capacity():

    assign_seats()

    if validate_final():
        print("\nAll seating constraints are satisfied.")
    else:
        print("\nWarning: All students could not be allocated valid seats.")

else:
    print("Please check student information or room capacity.")

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Check Capacity")
    print("5. Display Seating Plan")
    print("6. Search Student")
    print("7. Room-wise Summary")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        display_students()

    elif choice == "4":
        check_capacity()

    elif choice == "5":
        display_seating_plan()

    elif choice == "6":
        search_student()

    elif choice == "7":
        generate_room_summary()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
# Student Timetable Conflict Detection

# Timetable: (subject, day, start_time, end_time, room)
timetable = [
    ("Python", "Monday", 9, 11, "R101"),
    ("Maths", "Monday", 10, 12, "R102"),
    ("Physics", "Tuesday", 9, 11, "R101"),
    ("English", "Monday", 12, 13, "R101")
]

# Unavailable rooms
unavailable_rooms = ["R103", "R104"]

print("STUDENT TIMETABLE")
print("-" * 40)

# Display timetable
for subject, day, start, end, room in timetable:
    print(subject, day, str(start) + "-" + str(end), room)

print("\nCONFLICT DETECTION")
print("-" * 40)

# Check overlapping classes on the same day
for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        first = timetable[i]
        second = timetable[j]

        if first[1] == second[1]:
            if first[2] < second[3] and second[2] < first[3]:
                print("Time conflict:", first[0], "and", second[0])

# Check unavailable rooms
print("\nROOM VALIDATION")
print("-" * 40)

for subject, day, start, end, room in timetable:
    if room in unavailable_rooms:
        print(subject, "- Room", room, "is unavailable")

print("\nTIMETABLE VALIDATION")
print("-" * 40)

conflict_found = False

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        first = timetable[i]
        second = timetable[j]

        if first[1] == second[1]:
            if first[2] < second[3] and second[2] < first[3]:
                conflict_found = True

if conflict_found:
    print("Proposed timetable has conflicts.")
else:
    print("No time conflicts found.")
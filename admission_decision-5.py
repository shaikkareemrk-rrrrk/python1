
# University Admission Decision Engine

# Course requirements: [course, minimum aggregate, subject pass marks]
courses = [
    ["CSE", 75, 60],
    ["AIML", 70, 55],
    ["ECE", 65, 50]
]

# Applicants: (name, course, maths marks, physics marks, aggregate)
applicants = [
    ("Arun", "CSE", 85, 80, 88),
    ("Banu", "AIML", 70, 65, 78),
    ("Charan", "CSE", 65, 75, 76),
    ("Divya", "ECE", 60, 70, 72),
    ("Esha", "AIML", 80, 75, 78),
    ("Farhan", "ECE", 45, 80, 85)
]

eligible = []

print("UNIVERSITY ADMISSION DECISION")
print("-" * 50)

for name, course, maths, physics, aggregate in applicants:
    for course_name, minimum, subject_pass in courses:
        if course == course_name:
            break

    if maths < subject_pass or physics < subject_pass:
        print(name, "- Not eligible: Subject marks")
    elif aggregate < minimum:
        print(name, "- Not eligible: Aggregate marks")
    else:
        print(name, "- Eligible")
        eligible.append((name, course, aggregate, maths + physics))

# Rank eligible applicants by aggregate, then subject total
n = len(eligible)

for i in range(n):
    for j in range(0, n - i - 1):
        first = eligible[j]
        second = eligible[j + 1]

        if (first[2] < second[2] or
           (first[2] == second[2] and first[3] < second[3])):
            eligible[j], eligible[j + 1] = eligible[j + 1], eligible[j]

print("\nRANKED ELIGIBLE APPLICANTS")
print("-" * 50)

rank = 1

for name, course, aggregate, subject_total in eligible:
    print("Rank:", rank, "| Name:", name,
          "| Course:", course,
          "| Aggregate:", aggregate,
          "| Subject Total:", subject_total)
    rank = rank + 1

if len(eligible) == 0:
    print("No eligible applicants found.")

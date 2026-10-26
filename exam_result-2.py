
# Examination Result and Grace-Mark Validation

# Maximum marks and pass marks for each subject
subjects = [
    ["Python", 100, 40],
    ["Mathematics", 100, 40],
    ["English", 100, 35],
    ["Computer Science", 100, 40]
]

# Student marks: (subject name, marks obtained)
marks = [
    ("Python", 38),
    ("Mathematics", 65),
    ("English", 50),
    ("Computer Science", 39)
]

grace_limit = 2
total_marks = 0
maximum_total = 0
failed_subjects = 0
grace_used = 0
results = []

print("EXAMINATION RESULT")
print("-" * 55)

for subject, obtained in marks:
    for name, maximum, pass_marks in subjects:
        if subject == name:
            break

    grace = 0

    if obtained < 0 or obtained > maximum:
        print(subject, "- Invalid Marks")
        failed_subjects = failed_subjects + 1
        results.append((subject, obtained, "Invalid"))
        maximum_total = maximum_total + maximum
        continue

    if obtained < pass_marks:
        needed = pass_marks - obtained

        if needed <= grace_limit and grace_used + needed <= grace_limit:
            grace = needed
            grace_used = grace_used + needed
            obtained = obtained + grace

    if obtained >= pass_marks:
        status = "Pass"
    else:
        status = "Fail"
        failed_subjects = failed_subjects + 1

    results.append((subject, obtained, status))
    total_marks = total_marks + obtained
    maximum_total = maximum_total + maximum

    print(subject, "Marks:", obtained,
          "Pass Marks:", pass_marks,
          "Grace:", grace,
          "Status:", status)

print("-" * 55)
print("Total Marks:", total_marks, "/", maximum_total)
print("Grace Marks Used:", grace_used)

if failed_subjects == 0:
    percentage = total_marks / maximum_total * 100
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass Class")

    print("Final Result: PASS")
else:
    print("Failed/Invalid Subjects:", failed_subjects)
    print("Final Result: NOT PASSED")

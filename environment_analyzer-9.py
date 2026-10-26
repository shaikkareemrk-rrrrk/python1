# Environmental Monitoring Data Analyzer

# Air-quality readings for 3 locations over 4 days
readings = [
    [40, 55, 70, 45],
    [80, 90, 65, 75],
    [30, 35, 25, 40]
]

locations = ["Location A", "Location B", "Location C"]

# Threshold values
safe_limit = 50
moderate_limit = 75

print("ENVIRONMENTAL MONITORING REPORT")
print("-" * 40)

all_readings = []

for i in range(len(readings)):
    total = 0

    print("\n", locations[i])

    for j in range(len(readings[i])):
        value = readings[i][j]
        total = total + value
        all_readings.append(value)

        # Classify readings
        if value <= safe_limit:
            print(value, "- Safe")
        elif value <= moderate_limit:
            print(value, "- Moderate")
        else:
            print(value, "- Poor")

    average = total / len(readings[i])
    print("Average:", round(average, 2))

# Find maximum and minimum readings
highest = max(all_readings)
lowest = min(all_readings)

print("\nOVERALL ANALYSIS")
print("-" * 40)
print("Average reading:", round(sum(all_readings) / len(all_readings), 2))
print("Highest reading:", highest)
print("Lowest reading:", lowest)
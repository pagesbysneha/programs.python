def attendance(total, attended):
    percentage = (attended / total) * 100

    if percentage >= 75:
        eligible = "Yes"
    else:
        eligible = "No"

    return percentage, eligible

total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage, eligible = attendance(total, attended)

print("Attendance Percentage =", percentage)
print("Eligible =", eligible)


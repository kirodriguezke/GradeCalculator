# Ask the user for their grade percentage
grade_percentage = float(input("Enter your grade percentage: "))

# Initialize vaiable letter
letter = ""
sign = ""

# Determine letter according to grade percentage
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

# Stretch challenge 1
if letter != "A" and letter != "F":
    last_digit = int(grade_percentage) % 10

    if last_digit >= 7:
        sign ="+"
    elif last_digit < 3:
        sign = "-"
    else:
        sign = ""

# Stretch challenge 2
## Special case for "A": it only can be "A" or "A-"
if letter == "A" and grade_percentage < 94:
    sign = "-"

# Print the letter grade with sign
print(f"Your letter grade is: {letter}{sign}")

# Has the user passed the course?
if grade_percentage >= 70:
    print("Congratulations, you passed the course!")
else:
    print("Unfortunately, you did not pass. Better luck next year!")


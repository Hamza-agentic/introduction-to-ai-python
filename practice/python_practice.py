# Combining variables, conditions, loops, lists, and functions
# Function to calculate average marks
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
  
# Student information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Subjects and marks
subjects = ["Python", "AI", "Database", "Programming"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Display student information
print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("\n--- Marks ---")
for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

# Calculate average
average = calculate_average(marks)
print("\nAverage Marks:", average)

# Check result
if average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Result: Fail")

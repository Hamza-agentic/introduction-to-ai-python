# Loops in Python
# 1. For loop
print("Numbers from 1 to 5:")
for number in range(1, 6):
    print(number)

# 2. Loop through a list
print("\nMy favorite programming languages:")
languages = ["Python", "C++", "C#", "JavaScript"]
for language in languages:
    print(language)

# 3. While loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Done!")

# 4. Nested loop
print("\nMultiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)

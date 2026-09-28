# Demonstrating Python Functions
# 1. Simple function
def greet():
    print("Hello! Welcome to Python programming.")
greet()

# 2. Function with parameters
def greet_user(name):
    print("Hello", name)
greet_user("Hamza")

# 3. Get User ID from user
def get_user_id():
    user_id = input("Enter your user ID: ")
    print("Your User ID is:", user_id)
get_user_id()

# 3. Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print("Sum:", result)
add_numbers(10, 20)


# 4. Function that returns a value
def multiply_numbers(a, b):
    return a * b
answer = multiply_numbers(5, 4)
print("Multiplication:", answer)


# 5. Function with if-else
def check_number(number):
    if number > 0:
        return "Positive number"
    elif number < 0:
        return "Negative number"
    else:
        return "Zero"
print(check_number(10))
print(check_number(-5))
print(check_number(0))

# 6. Function using a list
def show_languages(languages):
    print("\nProgramming Languages:")
    for language in languages:
        print("-", language)
languages = ["Python", "C++", "C#", "Java"]
show_languages(languages)

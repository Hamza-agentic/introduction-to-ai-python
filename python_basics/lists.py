# Lists in Python
# 1. Creating a list
languages = ["Python", "C++", "C#", "JavaScript"]
print("Programming Languages:")
print(languages)
# 2. Accessing list items
print("\nFirst language:", languages[0])
print("Second language:", languages[1])
print("Last language:", languages[-1])

# 3. Changing an item
languages[2] = "Java"
print("\nAfter changing C# to Java:")
print(languages)

# 4. Adding an item
languages.append("C")
print("\nAfter adding C:")
print(languages)

# 5. Removing an item
languages.remove("C++")
print("\nAfter removing C++:")
print(languages)

# 6. Length of a list
print("\nNumber of languages:", len(languages))

# 7. Looping through a list
print("\nLanguages in the list:")

for language in languages:
    print(language)

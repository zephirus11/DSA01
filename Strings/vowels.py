# Example code for string methods

# Creating a string
my_string = "Hello, World!"

# Length of the string
length = len(my_string)
print("Length:", length)

# Converting to uppercase
uppercase = my_string.upper()
print("Uppercase:", uppercase)

# Converting to lowercase
lowercase = my_string.lower()
print("Lowercase:", lowercase)

# Counting occurrences of a substring
count = my_string.count("o")
print("Count:", count)

# Checking if the string starts with a specific substring
starts_with = my_string.startswith("Hello")
print("Starts with 'Hello':", starts_with)

# Checking if the string ends with a specific substring
ends_with = my_string.endswith("World!")
print("Ends with 'World!':", ends_with)

# Finding the index of a substring
index = my_string.index("World")
print("Index of 'World':", index)

# Replacing a substring
replaced = my_string.replace("Hello", "Hi")
print("Replaced:", replaced)

# Splitting the string into a list of substrings
split_list = my_string.split()
print("Split List:", split_list)

# Stripping leading and trailing whitespace
stripped = my_string.strip()
print("Stripped:", stripped)

# Checking if the string is alphanumeric
is_alphanumeric = my_string.isalnum()
print("Is Alphanumeric:", is_alphanumeric)

# Checking if the string is numeric
is_numeric = my_string.isnumeric()
print("Is Numeric:", is_numeric)

# Checking if the string is in titlecase
is_titlecase = my_string.istitle()
print("Is Titlecase:", is_titlecase)

# Checking if all characters in the string are uppercase
is_uppercase = my_string.isupper()
print("Is Uppercase:", is_uppercase)

# Checking if all characters in the string are lowercase
is_lowercase = my_string.islower()
print("Is Lowercase:", is_lowercase)
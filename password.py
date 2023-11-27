# Import the random and string modules
import random
import string

# Define the length and the types of characters for the password
length = 18

# You can change this to any number you want
chars = string.ascii_letters + string.digits + string.punctuation # You can modify this to include or exclude certain characters
print(chars)
# Generate a random password by choosing a character from the chars string for each position
password = ""
for i in range(length):
  password += random.choice(chars)

# Print the password
print("Your password is:", password)

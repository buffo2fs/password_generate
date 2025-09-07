import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbol=True):

    # Build the character set based on user choices
    characters_sets = []
    if use_uppercase:
        characters_sets.append(string.ascii_uppercase) #ABCD
    if use_lowercase:
        characters_sets.append(string.ascii_lowercase) #abcd
    if use_numbers:
        characters_sets.append(string.digits) #0123456789
    if use_symbol:
        characters_sets.append(string.punctuation) #@$%!&
    
    if not characters_sets:
        return "Error: No character types selected!"
    

    # Ensure at least one character from each selected set
    password_chars = [random.choice(char_set) for char_set in characters_sets]

    # Fill the rest of the password
    all_chars = ''.join(characters_sets)
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(random.choice(all_chars))
    
    # Shuffle to mix characters
    random.shuffle(password_chars)

    return ''. join(password_chars)

# User input
try:
    length = int(input("Enter password lenght: "))
    if length <= 0:
        raise ValueError("Length must be positive.")

except ValueError as e:
    print("Invalid input:", e)
    exit()

use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbol = input("Include symbols? (y/n): ").lower() == 'y'


# Generate password
password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbol)
print(f"Generated password: {password}")
    

    
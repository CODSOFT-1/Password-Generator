import random
import string

# Function to generate a password
def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function to get user input and generate the password
def main():
    print("Welcome to the Password Generator!")
    
    # Get desired password length from the user
    length = int(input("Enter the desired password length: "))

    if length < 6:
        print("Password length should be at least 6 characters for better security.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == '__main__':
    main()

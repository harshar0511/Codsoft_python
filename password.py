import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.ascii_letters.lower()
    else:
        print("Invalid complexity level. Please choose 'easy', 'medium', or 'hard'.")
        return None

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    
    while True:
        length = int(input("Enter the desired password length: "))
        complexity = input("Enter the complexity level ('easy', 'medium', or 'hard'): ")

        password = generate_password(length, complexity)
        if password:
            print("Generated Password:", password)

        try_again = input("Generate another password? (yes/no): ")
        if try_again.lower() != "yes":
            break
import random
import string

print("Enter the length of password(minimum 8 characters):")
length=int(input())
def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Generate a password with given length

    password = generate_password(length)
    print("Generated Password:", password)

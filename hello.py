# Simple Python Program

# Ask the user for their information
name = input("What is your name? ")
age = input("How old are you? ")
email = input("Please insert a valid email: ")
address = input("What is your address? ")

# Define the function
def print_info(Name, age, email, address):
    print("Hello, " + Name + "! Nice to meet you.")
    print("My Age: " + age + ".")
    print("My address is: " + address + ".")
    print("Your Email address is: " + email + ".")

# Call the function
print_info(name, age, email, address)

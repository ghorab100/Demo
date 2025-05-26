# Simple Python Program with Basic Input Validation
def WeclomeMessage():
  print("Welcome to our app.")
    
def is_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name and all(ch.isalpha() or ch == " " for ch in name):
            if name[0].isupper():
                return name
            else:
                print("Name must start with a capital letter.")
        else:
            print("Sorry, name can contain only letters and spaces!")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")

def get_valid_email(prompt):
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email and len(email) >= 5:
            return email
        print("Invalid email format. Please enter a valid email address.")

def get_valid_age(prompt):
    while True:
        age = input(prompt).strip()
        if age.isdigit() and 0 < int(age) < 100:
            return age
        print("Please enter a valid age as a number between 1 and 99.")

def get_marital_status(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        print("Please answer with 'yes' or 'no'.")

# Get validated inputs
WeclomeMessage() 

name = is_valid_name("What is your name? ")
age = get_valid_age("How old are you? ")
email = get_valid_email("Please insert a valid email: ")
address = get_non_empty_input("What is your address? ")
married = get_marital_status("Are you married (yes or no)? ")

# Define the function
def print_info(name, age, email, address, married):

    print(f"\nHello, {name}! Nice to meet you.")
    print(f"My Age: {age}.")
    print(f"My address is: {address}.")
    print(f"Your Email address is: {email}.")
    status = "Married" if married else "Single"
    print(f"Your status is: {status}.")

# Call the function
print_info(name, age, email, address, married)

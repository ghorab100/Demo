# Simple Python Program

# Ask the user for their information
name = input("What is your name? ")
age = input("How old are you? ")
email = input("Please insert a valid email: ")
address = input("What is your address? ")

married_input = input("Are you married (yes or no)? ")

# Convert to boolean
if married_input.lower() == "yes":
    married = True
else:
    married = False

# Define the function
def print_info(name, age, email, address, married):
    print("Hello, " + name + "! Nice to meet you.")
    print("My Age: " + age + ".")
    print("My address is: " + address + ".")
    print("Your Email address is: " + email + ".")
    
    # Convert boolean to string for printing
    if married :
        status = "Married"
    else :
        status = "Single"
    
    print("Your status is: " + status + ".")

# Call the function
print_info(name, age, email, address, married)

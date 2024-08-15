# A starter command line program for Python
# Input name
name = input("Enter your name: ")

# Check if the name is WhitzardX
if name == "WhitzardX":
    print(f"Hello {name}, what would you like to change?")
    
    # Get user response
    response = input()
    
    # Check if the response is about customizing the repo
    if response.lower() == "i want to customize the repo":
        print("Great! Let's work on customizing the repository.")
    else:
        print("Okay, let's see what else we can do.")
else:
    # If the name is not WhizardX, ask further if "no" is typed
    print("Go away.")
    further_response = input("Type 'no' to explain why: ")
    
    # If "no" is typed, ask why
    if further_response.lower() == "no":
        print("Why?")

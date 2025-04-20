

#Creating a function to read and modify a file

def read_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("\n--- File Content ---")
            print(data)
            # Example modification: convert to uppercase
            modified_data = data.upper()
            print("\n--- Modified Content ---")
            print(modified_data)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")

# Get the user's input
filename = input("What is the path of the file to be read? ")
read_modify_file(filename)

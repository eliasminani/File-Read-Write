# Program to read a file, modify its content, and write to a new file

def modify_content(text):
    """
    Modify the text in some way.
    For example, convert it to uppercase.
    You can change this logic if you want other transformations.
    """
    return text.upper()

try:
    # Ask user for input filename
    filename = input("Enter the name of the file to read: ")

    # Try opening the file for reading
    with open(filename, 'r') as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"✅ File has been successfully modified and saved as '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: The file you entered was not found. Please check the filename and try again.")

except PermissionError:
    print("❌ Error: Permission denied. You don’t have access to read this file.")

except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")

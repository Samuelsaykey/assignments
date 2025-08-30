def read_and_write_file():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Write the modified content into a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File has been read and modified content saved to 'output.txt'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    read_and_write_file()

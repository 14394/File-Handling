try:
    with open("my_file.txt", "w") as file:
        file.write("First line\n")
        file.write("Second line\n")
        file.write("Third line\n")
except IOError as e:
    print("Error occurred while creating the file:", e)

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Contents of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

try:
    with open("my_file.txt", "a") as file:
        file.write("Fourth line\n")
        file.write("Fifth line\n")
        file.write("Sixth line\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Task completed successfully.")
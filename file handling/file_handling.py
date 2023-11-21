# 1. Introduction to File Handling
    # 1.1 Overview
    # 1.2 File types
        # .py, .txt, .sh, .c, .doc, .jpg, .pdf
    # 1.3 File modes
        # Read, Write, Append
    # 1.4 Closing files
        # Open/Close
    # 1.5 Questions

# 2. Opening and Closing Files
    # 1.1 Using open() and close() methods

#     OPENING MODES:
#     r -> Read only mode | If not exist raise error
#     w -> Write (replace the current file) | If not exist creating a new file
#     a -> Append (adding the data to the current file) | If not exist creating a new file
#     x -> Creating a new file only if not exist | If EXIST raise error

my_file = open("test.txt")
my_file.close()

    # 1.2 Using 'with:' statement
with open("test.txt", "r") as my_file:
    my_file.read()

# 3. Reading from a File
    # 3.1 Reading entire file using read() method
with open("test.txt", "r") as my_file:
    print(my_file.read())
    index = 1
    for line in my_file:
        print(index, line)
        index += 1
    # 3.2 Reading lines using readline() for reading entire line
    print(my_file.readline())
    print(my_file.readline())
    # 3.3 Reading lines into a list using readlines() and iterate over it
    file_lines = my_file.readlines()
    print(type(file_lines))

# 4. Writing to a File
    # 4.1 Writing content using 'w' mode and 'a' mode
    # 4.2 Writing multiple lines using writelines().
    # 4.3 Discuss file pointers? seek() and tell() methods
    # 4.4 Questions

# 5. Practical Examples
    # 8.1 JSON files 
    # 8.2 CSV files
    # 8.3 Questions

# 6. Exercise/Hands-on Practice
# 7. Handling Exceptions during File Operations 
# 8. Working with Binary Files

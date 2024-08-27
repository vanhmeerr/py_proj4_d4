import os


counter = 0
def increment_counter():
    global counter
    counter += 1
    print(f"Global counter after incrementing: {counter}")

def reset_counter():
    counter = 0
    print(f"Local counter after resetting: {counter}")

increment_counter()
increment_counter()
increment_counter()

reset_counter()

# print the global counter after each function call
print(f"Global counter after reset_counter: {counter}")

print("<====================================>")


# print the current working directory
# print(f"Current working directory: {os.getcwd()}")

# # list all files and directories in the current working directory
# print(f"Files and Directories in the current working directory: {os.listdir()}")

# # create a new directory called test_dir
# os.mkdir("test_dir")

# # change the working directory to test_dir
# os.chdir("test_dir")

# # print the new working directory
# print(f"New working directory: {os.getcwd()}")

# # create a new file named test_file.txt inside test_dir
# with open("test_file.txt", "w") as f:
#     f.write("Hello World!")

# # After completing the above operations, delete test_file.txt and test_dir
# os.remove("test_file.txt")
# os.rmdir("test_dir")

def divide_number(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    finally :
        print("The division operation is complete.")

result = divide_number(10, 0)

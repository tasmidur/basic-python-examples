# python_examples.py

# Example 1: Variables and Data Types
def variables_and_data_types():
    name = "Alice"  # String
    age = 30        # Integer
    height = 5.5    # Float
    is_student = True  # Boolean

    print("Example 1: Variables and Data Types")
    print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}\n")

# Example 2: Control Structures (if-else)
def control_structures():
    number = 10
    print("Example 2: Control Structures (if-else)")
    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is zero.")
    print()

# Example 3: Loops (for and while)
def loops():
    print("Example 3: Loops")
    print("For Loop:")
    for i in range(5):
        print(f"Iteration {i + 1}")

    print("\nWhile Loop:")
    count = 0
    while count < 5:
        print(f"Count is {count}")
        count += 1
    print()

# Example 4: Functions
def add_numbers(a, b):
    return a + b

def functions():
    print("Example 4: Functions")
    result = add_numbers(5, 7)
    print(f"The sum of 5 and 7 is: {result}\n")

# Example 5: Lists
def lists():
    fruits = ["apple", "banana", "cherry"]
    print("Example 5: Lists")
    print("Fruits List:", fruits)
    fruits.append("orange")
    print("After adding orange:", fruits)
    print()

# Example 6: Dictionaries
def dictionaries():
    student = {
        "name": "Bob",
        "age": 22,
        "major": "Computer Science"
    }
    print("Example 6: Dictionaries")
    print("Student Dictionary:", student)
    print("Student Name:", student["name"])
    print()

# Example 7: Exception Handling
def exception_handling():
    print("Example 7: Exception Handling")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    print()

# Example 8: File I/O
def file_io():
    print("Example 8: File I/O")
    with open("example.txt", "w") as file:
        file.write("Hello, this is a test file.\n")
    
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
    print()



# Main function to run all examples
def main():
    variables_and_data_types()
    control_structures()
    loops()
    functions()
    lists()
    dictionaries()
    exception_handling()
    file_io()

# Entry point of the program
if __name__ == "__main__":
    main()
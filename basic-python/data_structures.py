# data_structures.py

# Example 1: Lists
def lists_example():
    print("Example 1: Lists")
    fruits = ["apple", "banana", "cherry"]
    print("Original List:", fruits)

    # Adding an item
    fruits.append("orange")
    print("After appending 'orange':", fruits)

    # Removing an item
    fruits.remove("banana")
    print("After removing 'banana':", fruits)

    # Accessing items
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])
    print("List length:", len(fruits))
    print()

# Example 2: Tuples
def tuples_example():
    print("Example 2: Tuples")
    colors = ("red", "green", "blue")
    print("Original Tuple:", colors)

    # Accessing items
    print("First color:", colors[0])
    print("Last color:", colors[-1])
    print("Tuple length:", len(colors))
    print()

# Example 3: Sets
def sets_example():
    print("Example 3: Sets")
    unique_numbers = {1, 2, 3, 4, 5}
    print("Original Set:", unique_numbers)

    # Adding an item
    unique_numbers.add(6)
    print("After adding 6:", unique_numbers)

    # Removing an item
    unique_numbers.remove(3)
    print("After removing 3:", unique_numbers)

    # Sets do not allow duplicates
    unique_numbers.add(2)
    print("After trying to add 2 again:", unique_numbers)
    print()

# Example 4: Dictionaries
def dictionaries_example():
    print("Example 4: Dictionaries")
    student = {
        "name": "Alice",
        "age": 21,
        "major": "Computer Science"
    }
    print("Original Dictionary:", student)

    # Accessing items
    print("Student Name:", student["name"])
    print("Student Age:", student["age"])

    # Adding a new key-value pair
    student["graduation_year"] = 2023
    print("After adding graduation year:", student)

    # Removing a key-value pair
    del student["age"]
    print("After removing age:", student)
    print()

# Main function to run all examples
def main():
    lists_example()
    tuples_example()
    sets_example()
    dictionaries_example()

# Entry point of the program
if __name__ == "__main__":
    main()
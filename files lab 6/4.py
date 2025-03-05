import os

def count_lines(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
filepath = input("Enter the file path: ")
num_lines = count_lines(filepath)
if num_lines is not None:
    print(f"The file '{filepath}' has {num_lines} lines.")

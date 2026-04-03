import os
import sys

def print_tree(directory, prefix="", depth=3, current_depth=0):
    # Stop recursion if we exceed the allowed depth
    if current_depth > depth:
        return

    # Get the contents of the directory
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"{prefix} [Permission Denied]")
        return

    # Sort to keep the output consistent
    items.sort()
    
    count = len(items)
    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = (i == count - 1)
        
        # Select the branch character
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{item}")
        
        # If it's a directory, recurse into it
        if os.path.isdir(path):
            # If it's the last item, the next level needs empty space
            # Otherwise, it needs a vertical pipe
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, new_prefix, depth, current_depth + 1)

def main():
    # Basic argument validation
    if len(sys.argv) < 2:
        print("Usage: python script.py <folder_path> [depth]")
        return

    target_folder = sys.argv[1]
    
    # Set a safe default depth of 2 (shows folder and immediate children)
    # or use the provided argument.
    max_depth = 2
    if len(sys.argv) > 2:
        try:
            max_depth = int(sys.argv[2])
        except ValueError:
            print("Warning: Depth must be an integer. Using default depth: 2")

    if not os.path.isdir(target_folder):
        print(f"Error: {target_folder} is not a valid directory.")
        return

    print(f"{os.path.abspath(target_folder)}")
    print_tree(target_folder, depth=max_depth)

if __name__ == "__main__":
    main()
